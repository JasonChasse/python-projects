import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
for i in range(10) :
	GPIO.output(18, GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(18, GPIO.LOW)
	time.sleep(.1)

	GPIO.output(23, GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(23, GPIO.LOW)
	time.sleep(.1)

	GPIO.output(18, GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(18, GPIO.LOW)
	time.sleep(.1)

	GPIO.output(23, GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(23, GPIO.LOW)
	time.sleep(.1)

	GPIO.output(18, GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(18, GPIO.LOW)
	time.sleep(.1)

	GPIO.output(23, GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(23, GPIO.LOW)
	time.sleep(.1)




