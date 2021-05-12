import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup relay output
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)

# Setup PIR input
GPIO.setup(14, GPIO.IN)

# Setup Speaker output
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)

while True :
    if  GPIO.input(14) == 1:
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)

    else :
        GPIO.input(14) == 0
        GPIO.output(15, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)

GPIO.cleanup()
