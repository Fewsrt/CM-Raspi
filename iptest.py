import socket
import time
import blynklib

BLYNK_AUTH = 'nD-SwPo3-WpMrvAbdksIFa4YnP14l9-A'
blynk = blynklib.Blynk(BLYNK_AUTH)

while True:
    blynk.run()
    testIP = "8.8.8.8"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((testIP, 0))
    ipaddr = s.getsockname()[0]
    host = socket.gethostname()
    blynk.virtual_write(5, str(ipaddr))
    blynk.virtual_write(6, str(host))
    print ("IP:", ipaddr, " Host:", host)
    time.sleep(3600)
