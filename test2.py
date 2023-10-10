import RPi.GPIO as GPIO
import time
import keyboard

def test(pin):
  print(pin)

# Define GPIO pins for the keypad
C1 = 8
C2 = 7
C3 = 1
C4 = 16

L1 = 0
L2 = 5
L3 = 6
L4 = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup([L1, L2, L3, L4], GPIO.OUT)
GPIO.setup([C1, C2, C3, C4], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def readLine(line, characters):
  GPIO.output(line, GPIO.HIGH)
  if(GPIO.input(C1) == 1):
          print(characters[0])
  if(GPIO.input(C2) == 1):
              print(characters[1])
  if(GPIO.input(C3) == 1):
          print(characters[2])
  if(GPIO.input(C4) == 1):
          print(characters[3])
  GPIO.output(line, GPIO.LOW)

try:
  while True:
    readLine(L1, ["1","2","3","A"])
    readLine(L2, ["4","5","6","B"])
    readLine(L3, ["7","8","9","C"])
    readLine(L4, ["*","0","#","D"])
    time.sleep(0.1)
except KeyboardInterrupt:
	print("\nApplication stopped!")