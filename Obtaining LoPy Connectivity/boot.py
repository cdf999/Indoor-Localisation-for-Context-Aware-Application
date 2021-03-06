import machine
from network import WLAN
wlan = WLAN() # get current object, without changing the mode

if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(mode=WLAN.STA)
    # configuration below MUST match your home router settings!!
    wlan.ifconfig(config=('dhcp'))

if not wlan.isconnected():
    # change the line below to match your network ssid, security and password
    wlan.connect('TelstraD293DF', auth=(WLAN.WPA2, 'alerteabrutus'), timeout=5000)
    while not wlan.isconnected():
        machine.idle() # save power while waiting

print(wlan.ifconfig())