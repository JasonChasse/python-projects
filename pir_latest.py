import RPi.GPIO as GPIO 
import time
import os



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup relay output
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)

# Setup PIR input
GPIO.setup(14, GPIO.IN)


while True :
    i=GPIO.input(14)
    
    if i==0:      
        GPIO.output(15, GPIO.LOW)
        time.sleep(2)
        print('No intruder detected')
        
        
        
        
    elif i==1:
        GPIO.output(15, GPIO.HIGH)
        time.sleep(3)
        print('INTRUDER ALERT')
        myCmd1 = 'omxplayer -o local brokein.wav'
        myCmd2 = 'omxplayer -o local smg.wav'
        myCmd3 = 'omxplayer -o local smg.wav'
        myCmd4 = 'omxplayer -o local smg.wav'
        os.system(myCmd1)
        os.system(myCmd2)
        os.system(myCmd3)
        os.system(myCmd4)
        
        
        
        
GPIO.cleanup()
              