#import libraries
import time
import RPi.GPIO as GPIO

#GPIO setup -- pin 8 as moisture sensor ouput
#GPIO setup -- pin 10 as pump output
#GPIO setup -- pin 11 as moisture sensor input
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(11,GPIO.IN)

water = 10
try:
    while True:
        time.sleep(2)
        GPIO.output(8,False)
        if (GPIO.input(11))==0:
            print('Wet')
            GPIO.output(10,True)
            time.sleep(5)
            break
        elif (GPIO.input(11))==1:
            print('Plant is dry')
            time.sleep(2)
            print('activating the pump...')
            time.sleep(2)
            GPIO.output(10,False)
            time.sleep(3)
            break

finally:
    #cleanup the GPIO pins before ending
    GPIO.cleanup()
