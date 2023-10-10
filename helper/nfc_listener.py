import time
import binascii
from pn532pi import Pn532, pn532
from pn532pi import Pn532Hsu
import time
import threading

PN532_HSU = Pn532Hsu(0)
nfc = Pn532(PN532_HSU)

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
        # self.nfc_thread = threading.Thread(target=self._listen_thread, args=(callback,))
        # self.nfc_thread.start()
        self._listen_thread(callback)
    
    def _listen_thread(self, callback):
        while self.listening:
            time.sleep(0.3)
            success, id = self.scan_for_card()
            print(f"LOGGER::NFC Listening")
            if success:
                break
        if id:
            self.listening = False
            callback(id)
    
    def stop_listen(self):
        self.listening = False
        if self.nfc_thread:
            self.nfc_thread.join()
            print(f"LOGGER::NFC Stop Listening")
