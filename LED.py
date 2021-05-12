import RPi.GPIO as GPIO
import time
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.HIGH)
time.sleep(5)
print "LED off"
GPIO.output(18,GPIO.LOW)
