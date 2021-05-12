import RPi.GPIO as GPIO 
import time
import os
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup PIR input
GPIO.setup(12, GPIO.IN)

while True :
    i=GPIO.input(12)
    
    if i==0:      
        print('No intruder detected')

    elif i==1:
        print('INTRUDER ALERT')
        f=open("intruderalert.txt",'a')
        f.write ("Intruder Alert" '\n')
        f.write(datetime.datetime.now().ctime())
        f.write('\n')
        f.write('\n')
        f.close
