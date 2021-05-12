import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(24, GPIO.HIGH)
time.sleep(2)

GPIO.output(24, GPIO.LOW)
time.sleep(2)

GPIO.output(24, GPIO.HIGH)
time.sleep(4)

GPIO.output(24, GPIO.LOW)
time.sleep(2)

GPIO.output(24, GPIO.HIGH)
time.sleep(8)

GPIO.output(24, GPIO.LOW)
time.sleep(2)

GPIO.output(24, GPIO.HIGH)
time.sleep(16)

GPIO.output(24, GPIO.LOW)
time.sleep(2)

