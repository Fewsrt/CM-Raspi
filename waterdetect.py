import time
import blynklib
import RPi.GPIO as GPIO

BLYNK_AUTH = 'nD-SwPo3-WpMrvAbdksIFa4YnP14l9-A'
blynk = blynklib.Blynk(BLYNK_AUTH)

channel = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

while True:
    if GPIO.input(channel):
        print("No Water Detected!")
        blynk.virtual_write(0, "No Water Detected!")
        blynk.virtual_write(1, 0)
    else:
        print("Water Detected!")
        blynk.virtual_write(0, "Water Detected!")
        blynk.virtual_write(1, 255) 

time.sleep(5)