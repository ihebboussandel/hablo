import pyaudio
import wave
import audioop
from collections import deque
import os
import requests
from requests.auth import HTTPBasicAuth
import time
import math

LANG_CODE = 'en-US'  # Language to use

GOOGLE_SPEECH_URL = 'https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&pfilter=2&lang=%s&maxresults=6' % (LANG_CODE)
HABLO_BRAINS= 'http://tuleap.odc.tn/restApi/Hablo_v1/hard/'
#FLAC_CONV = 'flac '  # Path to flac.exe for wav to flac coversion.
                       # on Linux
AUDIO_PATH="/var/www/html/audio/"
# Microphone stream config.
CHUNK =  2048 # CHUNKS of bytes to read each time from mic
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
THRESHOLD = 11750 # The threshold intensity that defines silence
                  # and noise signal (an int. lower than THRESHOLD is silence).

SILENCE_LIMIT = 6  # Silence limit in seconds. The max ammount of seconds where
                   # only silence is recorded. When this time passes the
                   # recording finishes and the file is delivered.

PREV_AUDIO = 1    #0.5  # Previous audio (in seconds) to prepend. When noise
                  # is detected, how much of previously recorded audio is
                  # prepended. This helps to prevent chopping the beggining
                  # of the phrase.
WAVE_SAMPLERATE =48000

def read_values():
     f= open("/var/www/html/logs/color_status.log","r+")
     #f=open("guru99.txt","a+")
     #for i in range(10):
     #    f.write("This is line %d\r\n" % (i+1))
     #f.close()   
     #Open the file back and read the contents
     #f=open("guru99.txt", "r")
     if f.mode == 'r': 
          contents =f.read()
          print contents
     #or, readlines reads the individual line into a list
     fl =f.readlines()
     #for x in fl:
     try:
         out=fl[0].split(':')
     except IndexError as error:
	  dummy="2:2:2"
          return dummy.split(':')
     return out

def write_values(g,r,b):
	f = open('/var/www/html/logs/color_status.log', 'w+')
	f.write(str(g)+':'+str(r)+':'+str(b))  # python will convert \n to os.linesep
	f.close()  # you can omit in most cases as the destructor will call it

Memory_Color=read_values()

def audio_int(chunk,num_samples):
    """ Gets average audio intensity of your mic sound. You can use it to get
        average intensities while you're talking and/or silent. The average
        is the avg of the 20% largest intensities recorded.
    """

    print "calibrationg mic threchhold."
    values = [math.sqrt(abs(audioop.rms(chunk, 4))) 
              for x in range(num_samples)] 
    values = sorted(values, reverse=True)
    r = sum(values[:int(num_samples * 0.2)]) / int(num_samples * 0.2)
    #print " Finished "
    print " Average audio intensity is ", r
    return r


def listen_for_speech(threshold=THRESHOLD, num_phrases=-1):
    """
    Listens to Microphone, extracts phrases from it and sends it to 
    Google's TTS service and returns response. a "phrase" is sound 
    surrounded by silence (according to threshold). num_phrases controls
    how many phrases to process before finishing the listening process 
    (-1 for infinite). 
    """
    #Open stream
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print "* Listening mic. "
    audio2send = []
    cur_data = ''  # current chunk  of audio data
    rel = RATE/CHUNK
    slid_win = deque(maxlen=SILENCE_LIMIT * rel)
    #Prepend audio from 0.5 seconds before noise was detected
    prev_audio = deque(maxlen=PREV_AUDIO * rel) 
    started = False
    recalibration_counter=0
    n = num_phrases
    response = []
    #THRESHOLD=audio_int(stream.read(CHUNK, exception_on_overflow = False),CHUNK)+1000
    while (num_phrases == -1 or n > 0):
        cur_data = stream.read(CHUNK, exception_on_overflow = False)
        slid_win.append(math.sqrt(abs(audioop.rms(cur_data, 4))))
        #print slid_win[-1]
        if(sum([x > THRESHOLD for x in slid_win]) > 4):
            if(not started):
                print "Starting record of phrase"
		write_values(0,100,0)
                started = True
            audio2send.append(cur_data)
	    recalibration_counter= recalibration_counter+1
        elif (started is True):
            print "Finished"
            # The limit was reached, finish capture and deliver.
            filename =AUDIO_PATH+save_scream(list(prev_audio) + audio2send, p)
            # Send file to Google and get response
	    write_values(100,0,0)
            r = stt_google_wav(filename) 
            if num_phrases == -1:
                print "Response", r
		write_values(Memory_Color[0],Memory_Color[1],Memory_Color[2])
            else:
                response.append(r)
            # Remove temp file. Comment line to review.
            os.remove(filename)
            # Reset all
            started = False
	    write_values(Memory_Color[0],Memory_Color[1],Memory_Color[2])
            slid_win = deque(maxlen=SILENCE_LIMIT * rel)
            prev_audio = deque(maxlen=0.5 * rel) 
            audio2send = []
            n -= 1
            #print "Listening ..."
        else:
            prev_audio.append(cur_data)

    print "* Sropped stream"
    stream.close()
    p.terminate()

    return response


def save_scream(data, p):
    """ Saves mic data to temporary WAV file. Returns filename of saved 
        file """

    filename = 'output_'+str(int(time.time()))
    # writes data to WAV file
    data = ''.join(data)
    wf = wave.open(AUDIO_PATH+filename + '.wav', 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(WAVE_SAMPLERATE)  # TODO make this value a function parameter?
    wf.writeframes(data)
    wf.close()
    return filename + '.wav'


def stt_google_wav(audio_fname):
    """ Sends audio file (audio_fname) to Google's text to speech 
        service and returns service's response. We need a FLAC 
        converter if audio is not FLAC (check FLAC_CONV). """

    #print "Sending ", audio_fname
    #Convert to flac first
    filename = audio_fname

    # Headers. A common Chromium (Linux) User-Agent
    print HABLO_BRAINS+'1/uploadsFile'
    fin = open(filename ,'rb')
    files={'soundFile':fin}
    username='123'
    password='123'
    write_values(0,100,100)
    req = requests.post(HABLO_BRAINS+'1/uploadsFile',files=files ,auth=HTTPBasicAuth(username,password))
    print req.text
    print "Sending Resusst to hablo server "
    #print "response", response
    try:
        p = req.text
        response = p
        res = response
    except:
        print "Couldn't parse service response"
        res = None

    return res


if(__name__ == '__main__'):
    data = listen_for_speech()  # listen to mic.
    #print stt_google_wav('hello.flac')  # translate audio file
    #audio_int()  # To measure your mic levels
