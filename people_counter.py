# Counts people as they walk by PIR

import RPi.GPIO as GPIO
import time
import os

count=0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings{False)

# Setup PIR input
GPIO.setup(23, GPIO.IN)


while True :

    if :
        count == 100
        print("100 people capacity reached stop now.")
    
    elif GPIO.input(23) == 0 :
        print("No person detected!")

    else :
        count = count + 1
        print(count)
        time.sleep(2)
        GPIO.cleanup()
        

    


