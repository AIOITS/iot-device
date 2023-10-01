import time
import binascii
from pn532pi import Pn532, pn532
from pn532pi import Pn532I2c

PN532_I2C = Pn532I2c(1)
nfc = Pn532(PN532_I2C)

def setup():
    nfc.begin()
    versiondata = nfc.getFirmwareVersion()
    if not versiondata:
        print("Didn't find PN53x board")
        raise RuntimeError("Didn't find PN53x board")
    print("Found chip PN5 {:#x} Firmware ver. {:d}.{:d}".format((versiondata >> 24) & 0xFF, (versiondata >> 16) & 0xFF, (versiondata >> 8) & 0xFF))
    nfc.setPassiveActivationRetries(0xFF)
    nfc.SAMConfig()
    print("Waiting for an ISO14443A card")

def scan_for_card():
    success, uid = nfc.readPassiveTargetID(pn532.PN532_MIFARE_ISO14443A_106KBPS)
    if success:
        print("Found a card!")
        print("UID Length: {:d}".format(len(uid)))
        print("UID Value: {}".format(binascii.hexlify(uid)))
        return uid
    else:
        return False

def listen():
    while True:
        result = scan_for_card()
        if result : return result
        time.sleep(1)
    
setup()
listen()