import blynklib

BLYNK_AUTH = 'nD-SwPo3-WpMrvAbdksIFa4YnP14l9-A'
blynk = blynklib.Blynk(BLYNK_AUTH)

while True:
    blynk.run()
    blynk.virtual_write(1, 25.6)
    blynk.virtual_write(2, 90.6)
