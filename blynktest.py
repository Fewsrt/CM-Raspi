import Blynklib

BLYNK_AUTH = 'nD-SwPo3-WpMrvAbdksIFa4YnP14l9-A'
blynk = Blynklib.Blynk(BLYNK_AUTH)

while True:
    blynk.run()
    blynk.virtual_wirte(1)
