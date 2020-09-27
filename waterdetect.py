import time
import blynklib
import RPi.GPIO as GPIO

channel = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

while True:
    if GPIO.input(channel):
        print("No Water Detected!")
    else:
        print("Water Detected!")
