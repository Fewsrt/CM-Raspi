import socket
import time
import blynklib
from gpiozero import CPUTemperature

BLYNK_AUTH = 'nD-SwPo3-WpMrvAbdksIFa4YnP14l9-A'
blynk = blynklib.Blynk(BLYNK_AUTH)

while True:
    blynk.run()
    ip = readip()
    blynk.virtual_write(5, str(ip))


def readip(ipaddr, host):
    testIP = "8.8.8.8"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((testIP, 0))
    ipaddr = s.getsockname()[0]
    host = socket.gethostname()
    print ("IP:", ipaddr, " Host:", host)
    time.sleep(3600)
    return readip(ipaddr)
