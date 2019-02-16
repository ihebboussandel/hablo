import RPi.GPIO as GPIO
import threading
import time
import random
 
PINS = [12,33,32]  # R,G,B
 


def read_values():

     f= open("/var/www/html/logs/color_status.log","w+")
     #f=open("guru99.txt","a+")
     for i in range(10):
         f.write("This is line %d\r\n" % (i+1))
     f.close()   
     #Open the file back and read the contents
     #f=open("guru99.txt", "r")
     #   if f.mode == 'r': 
     #     contents =f.read()
     #     print contents
     #or, readlines reads the individual line into a list
     #fl =f.readlines()
     #for x in fl:
     #print x


 
def main():
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PINS, GPIO.OUT, initial=GPIO.LOW)
        print("\nPress ^C (control-C) to exit the program.\n")
        while True:
            select_and_set_next_pin()
            if all(GPIO.input(pin) == GPIO.LOW for pin in PINS):
                select_and_set_next_pin()
            time.sleep(0.75)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
 
 
def select_and_set_next_pin():
    next_pin = PINS[random.randint(0, 2)]
    GPIO.output(next_pin, not GPIO.input(next_pin))
 
 
if __name__ == '__main__':
    main()
    read_values()
