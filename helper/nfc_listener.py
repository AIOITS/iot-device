import time
import binascii
from pn532pi import Pn532, pn532
from pn532pi import Pn532I2c
import smbus
import time

PN532_I2C = Pn532I2c(1)
nfc = Pn532(PN532_I2C)

class NfcListener():
    def __init__(self) -> None:
        self.setup()
        self.listening = False

    def setup(self):
        nfc.begin()
        versiondata = nfc.getFirmwareVersion()
        if not versiondata:
            raise RuntimeError("Didn't find PN53x board")
        nfc.setPassiveActivationRetries(0xFF)
        nfc.SAMConfig()

    def scan_for_card(self):
        success, uid = nfc.readPassiveTargetID(pn532.PN532_MIFARE_ISO14443A_106KBPS)
        if success:
            id = "{}".format(binascii.hexlify(uid).decode('utf-8'))
            return True, id
        else:
            return False, None

    def listen(self, callback):
        self.listening = True
        bus = smbus.SMBus(1)
        id = None
        while self.listening:
            time.sleep(1)
            success, id = self.scan_for_card()
            if success: break
        if id:
            self.listening = False
            callback(id)
    
    def stop_listen(self):
        self.listening = False