import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

solar_relay_pin = 9
bensin_relay_pin = 11

GPIO.setup(solar_relay_pin, GPIO.OUT)
GPIO.setup(bensin_relay_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(solar_relay_pin, GPIO.HIGH)
        GPIO.output(bensin_relay_pin, GPIO.LOW)
        print("Relay ON")
        
        time.sleep(5)
        
        GPIO.output(solar_relay_pin, GPIO.LOW)
        GPIO.output(bensin_relay_pin, GPIO.HIGH)
        print("Relay OFF")
        
        time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()
