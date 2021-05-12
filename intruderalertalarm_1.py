import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

#Set pin 16 as an output, and set servo1 as pin 16 as PWM
GPIO.setup(16, GPIO.OUT)

#setup relay output
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)

#setup pin 4 as output
GPIO.setup(4, GPIO.OUT)

servo1 = GPIO.PWM(16,50) #50 = 50 HZ Pulse

#Setup PIR input
GPIO.setup(12, GPIO.IN)

while True :
        i=GPIO.input(12)
        
        if i==0:
            GPIO.output(26, GPIO.LOW)
            time.sleep(.5)
            print('No Intruder Detected')

        elif i==1:
            GPIO.output(26, GPIO.HIGH)
            time.sleep(.1)
            GPIO.output(26, GPIO.LOW)
            time.sleep(.1)
            GPIO.output(26, GPIO.HIGH)
            time.sleep(.1)
            GPIO.output(26, GPIO.LOW)
            time.sleep(.1)
            GPIO.output(26, GPIO.HIGH)
            time.sleep(.1)
            GPIO.output(26, GPIO.LOW)
            time.sleep(.1)
            GPIO.output(26, GPIO.HIGH)
            time.sleep(.1)
            GPIO.output(26, GPIO.LOW)
            time.sleep(.1)
            GPIO.output(26, GPIO.HIGH)
            time.sleep(.2)
            
            GPIO.output(4, GPIO.HIGH)
            time.sleep(.1)
            GPIO.output(4, GPIO.LOW)
            time.sleep(.1)
            GPIO.output(4, GPIO.HIGH)
            time.sleep(.1)
            GPIO.output(4, GPIO.LOW)
            time.sleep(.1)
            GPIO.output(4, GPIO.HIGH)
            time.sleep(.1)
            GPIO.output(4, GPIO.LOW)
            time.sleep(.1)
            GPIO.output(4, GPIO.HIGH)
            time.sleep(.1)
            GPIO.output(4, GPIO.LOW)
            time.sleep(.1)        
            
            
            servo1.start(0)
            servo1.ChangeDutyCycle(2)
            time.sleep(.5)
            servo1.ChangeDutyCycle(10)
            time.sleep(.5)
            servo1.ChangeDutyCycle(2)
            time.sleep(.5)
            servo1.ChangeDutyCycle(10)
            time.sleep(.5)
            servo1.ChangeDutyCycle(2)
            time.sleep(.5)
            servo1.ChangeDutyCycle(6)
            time.sleep(1)
            servo1.start(0)
            #servo1.stop()            
            
            print('INTRUDER ALERT')
            myCmd1 = 'omxplayer -o local intruderalert.mp3'
            myCmd2 = 'omxplayer -o local intruderalert.mp3'
            myCmd3 = 'omxplayer -o local intruderalert.mp3'
            text_file = open("intruders.txt", "a")
            text_file.write("Intruder Detected \n  ")
            text_file.close()
            os.system(myCmd1)
            os.system(myCmd2)
            os.system(myCmd3)
            

GPIO.cleanup()
