import sys,getopt
import RPi.GPIO as GPIO
import threading
import time
import random
 
R = 12
G = 33
B = 32
 
PINS = [R,G,B]

 
def initialize_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PINS, GPIO.OUT, initial=GPIO.LOW)
 
 
def color_test(channel, frequency, speed, step):
    p = GPIO.PWM(channel, frequency)
    p.start(0)
    while True:
        for dutyCycle in range(0, 101, step):
            p.ChangeDutyCycle(dutyCycle)
            time.sleep(speed)
        for dutyCycle in range(100, -1, -step):
            p.ChangeDutyCycle(dutyCycle)
            time.sleep(speed)
 
 
def color_test_thread(frequancy=300,sR=0.2,sG=0.4,sB=0.5,sR_step=0,sG_step=0,sB_step=0):
    threads = []
    threads.append(threading.Thread(target=color_test, args=(R, frequancy, sR, sR_step)))
    threads.append(threading.Thread(target=color_test, args=(G, frequancy,sG, sG_step)))
    threads.append(threading.Thread(target=color_test, args=(B, frequancy, sB,sB_step)))
    for t in threads:
        t.daemon = True
        t.start()
    for t in threads:
        t.join()
 
 
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"c:rgb:",["rarg=","garg=","barg="])
    except getopt.GetoptError:
        print 'test.py -rgb <red color> <blue color> <green color>'
        sys.exit(2)
    try:
        initialize_gpio()
	for opt,arg in opts:
        	if opt =='-c':
		   print '-c argument'
		elif opt in('-r','--rarg'):
		   print '-r argument = ',arg
		elif opt in('-g','--garg'):
		   print '-g argument = ',arg
		elif opt in ('-b','--barg'):
		   print '-b argument = ',arg
        color_test_thread(0.01,0.0,0.0,0.0,12,1,5)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
 
 
if __name__ == '__main__':
    main(sys.argv[1:])
    #print sys.argv

