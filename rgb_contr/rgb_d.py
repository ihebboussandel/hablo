import random, time
import RPi.GPIO as GPIO
import colorsys
 
RUNNING = True
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
red = 12
green = 33
blue = 32
 
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)


Freq = 100
 
RED = GPIO.PWM(red, Freq)
RED.start(100)
GREEN = GPIO.PWM(green, Freq)
GREEN.start(100)
BLUE = GPIO.PWM(blue, Freq)
BLUE.start(100)

outval = 128
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

def wheel_color(position):
    """Get color from wheel value (0 - 384)."""
    
    if position < 0:
        position = 0
    if position > 384:
        position = 384

    if position < 128:
        r = 127 - position % 128
        g = position % 128
        b = 0
    elif position < 256:
        g = 127 - position % 128
        b = position % 128
        r = 0
    else:
        b = 127 - position % 128
        r = position % 128
        g = 0

    return r, g, b

try:
	
	'''for pos in range(0,385):
		r, g, b = wheel_color(pos)
		#print (r, g, b)
		percenttestr = (r/128.0)*100.0
		percenttestg = (g/128.0)*100.0
		percenttestb = (b/128.0)*100.0
		#print (percenttestr)
		#print (percenttestg)
		#print (percenttestb)
		RED.ChangeDutyCycle(percenttestr)
		GREEN.ChangeDutyCycle(percenttestg)
		BLUE.ChangeDutyCycle(percenttestb)
		time.sleep(0.02)'''
	while True:
		COLOR=read_values()
		RED.ChangeDutyCycle(float(COLOR[1]))
        	GREEN.ChangeDutyCycle(float(COLOR[0]))
        	BLUE.ChangeDutyCycle(float(COLOR[2]))
        	time.sleep(0.01)
			
except KeyboardInterrupt:
	GPIO.cleanup()
