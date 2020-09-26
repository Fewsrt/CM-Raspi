import blynklib

dhtDevice = adafruit_dht.DHT22(board.D24)

BLYNK_AUTH = 'nD-SwPo3-WpMrvAbdksIFa4YnP14l9-A'
blynk = blynklib.Blynk(BLYNK_AUTH)

while True:
    blynk.run()
    blynk.virtual_wirte(1)
