import RPi.GPIO as GPIO
import time
import keyboard
import threading

# Define GPIO pins for the keypad
L1 = 22
L2 = 27
L3 = 23
L4 = 24

C1 = 6
C2 = 8
C3 = 5
C4 = 7

class KeypadListener:
  def __init__(self):

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup([L1, L2, L3, L4], GPIO.OUT)
    GPIO.setup([C1, C2, C3, C4], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    self.update_thread = threading.Thread(target=self.listen_keypad)
    self.update_thread.daemon = True
    self.update_thread.start()

  def readLine(self, line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1): keyboard.press_and_release(characters[0])
    if(GPIO.input(C2) == 1): keyboard.press_and_release(characters[1])
    if(GPIO.input(C3) == 1): keyboard.press_and_release(characters[2])
    if(GPIO.input(C4) == 1): keyboard.press_and_release(characters[3])
    GPIO.output(line, GPIO.LOW)

  def listen_keypad(self):
    while True:
      self.readLine(L1, ["1","2","3","a"])
      self.readLine(L2, ["4","5","6","b"])
      self.readLine(L3, ["7","8","9","c"])
      self.readLine(L4, ["*","0","#","d"])
      time.sleep(0.3)