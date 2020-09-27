import blynklib

# cmsensor1
#BLYNK_AUTH = 'nD-SwPo3-WpMrvAbdksIFa4YnP14l9-A'

# cmsensor2
BLYNK_AUTH = 'JFDPBMufAg2aRnHmO5ITI9H29aUbZmA1'
blynk = blynklib.Blynk(BLYNK_AUTH)

WidgetTerminal terminal(V11);

while True:
    blynk.run()
    terminal.println(F("Blynk v" BLYNK_VERSION ": Device started"))