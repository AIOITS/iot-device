import RPi.GPIO as GPIO
from config.constant import *

class Pump():
  def __init__(self) -> None:
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(PIN_PERTAMAX_RELAY, GPIO.OUT)
    GPIO.setup(PIN_SOLAR_RELAY, GPIO.OUT)
    GPIO.setup(PIN_PERTALITE_RELAY, GPIO.OUT)
    
    self.turn_off_relay(PIN_SOLAR_RELAY)
    self.turn_off_relay(PIN_PERTALITE_RELAY)
    self.turn_off_relay(PIN_PERTAMAX_RELAY)
    
  def turn_on_relay(self, pin):
    print("turn on relay")
    GPIO.output(pin, GPIO.LOW)
    
  def turn_off_relay(self, pin):
    print("turn off relay")
    GPIO.output(pin, GPIO.HIGH)

  def get_fuel_pin(self, fuel_name: str):
    if fuel_name == "Solar / Biodiesel": return PIN_SOLAR_RELAY
    if fuel_name == "Pertalite": return PIN_PERTALITE_RELAY
    if fuel_name == "Pertamax": return PIN_PERTAMAX_RELAY