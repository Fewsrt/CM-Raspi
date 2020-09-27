import blynklib
import RPi.GPIO as GPIO

BLYNK_AUTH = 'nD-SwPo3-WpMrvAbdksIFa4YnP14l9-A'
blynk = blynklib.Blynk(BLYNK_AUTH)

channel = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


def callback(channel):
    if GPIO.input(channel):
        print("No Water Detected!")
        blynk.virtual_write(9, "No Water Detected!")
        blynk.virtual_write(1, 0)
    else:
        print("Water Detected!")
        blynk.virtual_write(9, "Water Detected!")
        blynk.virtual_write(1, 255)


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
    blynk.run()
    callback()
