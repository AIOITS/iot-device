#button
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #view pengguna, kanan atas
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #kanan tengah
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #kanan bawah
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #kiri atas
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #kiri tengah
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #kiri bawah
while True:
    if GPIO.input(18)==GPIO.HIGH:
        print("Button18 was pressed")
    if GPIO.input(23)==GPIO.HIGH:
        print("Button23 was pressed")
    if GPIO.input(24)==GPIO.HIGH:
        print("Button24 was pressed")
    if GPIO.input(17)==GPIO.HIGH:
        print("Button17 was pressed")
    if GPIO.input(27)==GPIO.HIGH:
        print("Button27 was pressed")
    if GPIO.input(22)==GPIO.HIGH:
        print("Button22 was pressed")
        
#keypad
import RPi.GPIO as GPIO
import time

# these GPIO pins are connected to the keypad
# change these according to your connections!
L1 = 22
L2 = 27
L3 = 24
L4 = 23

C1 = 6
C2 = 5
C3 = 8
C4 = 7

# Initialize the GPIO pins

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

# Make sure to configure the input pins to use the internal pull-down resistors

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# The readLine function implements the procedure discussed in the article
# It sends out a single pulse to one of the rows of the keypad
# and then checks each column for changes
# If it detects a change, the user pressed the button that connects the given line
# to the detected column

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
        # call the readLine function for each row of the keypad
        readLine(L1, ["1","2","3","A"])
        readLine(L2, ["4","5","6","B"])
        readLine(L3, ["7","8","9","C"])
        readLine(L4, ["*","0","#","D"])
        time.sleep(0.3)
except KeyboardInterrupt:
    print("\nApplication stopped!")

