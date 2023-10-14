import RPi.GPIO as GPIO

PIN_BUTTON_LEFT_TOP = 24
PIN_BUTTON_LEFT_MIDDLE = 23
PIN_BUTTON_LEFT_BOTTOM = 18
PIN_BUTTON_RIGHT_TOP = 17
PIN_BUTTON_RIGHT_MIDDLE = 27
PIN_BUTTON_RIGHT_BOTTOM = 22

class ButtonListener():
  def __init__(self) -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_BUTTON_LEFT_TOP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_BUTTON_LEFT_MIDDLE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_BUTTON_LEFT_BOTTOM, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_BUTTON_RIGHT_TOP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_BUTTON_RIGHT_MIDDLE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_BUTTON_RIGHT_BOTTOM, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

  def onPressed(self, pin, function):
    GPIO.remove_event_detect(pin)
    GPIO.add_event_detect(pin, GPIO.RISING, callback=function, bouncetime=500)
  
  def remove_onPressed(self, pin):
    GPIO.remove_event_detect(pin)
    
  def clear_onPressed(self):
    
    self.onPressed(PIN_BUTTON_LEFT_TOP, lambda pin: None)
    self.onPressed(PIN_BUTTON_LEFT_MIDDLE, lambda pin: None)
    self.onPressed(PIN_BUTTON_LEFT_BOTTOM, lambda pin: None)
    self.onPressed(PIN_BUTTON_RIGHT_TOP, lambda pin: None)
    self.onPressed(PIN_BUTTON_RIGHT_MIDDLE, lambda pin: None)
    self.onPressed(PIN_BUTTON_RIGHT_BOTTOM, lambda pin: None)