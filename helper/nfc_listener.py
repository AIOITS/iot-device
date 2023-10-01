import time
import binascii
from pn532pi import Pn532, pn532
from pn532pi import Pn532I2c

class NfcListener():
    PN532_I2C = Pn532I2c(1)
    nfc = Pn532(PN532_I2C)

    def __init__(self) -> None:
        self.setup()

    def setup(self):
        self.nfc.begin()
        versiondata = self.nfc.getFirmwareVersion()
        if not versiondata:
            raise RuntimeError("Didn't find PN53x board")
        self.nfc.setPassiveActivationRetries(0xFF)
        self.nfc.SAMConfig()

    def scan_for_card(self, callback):
        success, uid = self.nfc.readPassiveTargetID(pn532.PN532_MIFARE_ISO14443A_106KBPS)
        if success:
            id = "{}".format(binascii.hexlify(uid))
            callback(id)
            return True
        else:
            return False

    def listen(self, callback):
      while True:
        if self.scan_for_card(callback): break
        time.sleep(1)
