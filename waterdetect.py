import time
import blynklib
import RPi.GPIO as GPIO

channel = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


def callback(channel):
    if GPIO.input(channel):
        print("No Water Detected!")

    else:
        print("Water Detected!")


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(2)
