from tkinter import *
import tkinter as tk
from config.style import *
from config.constant import *
import pages.init as ps
from helper.api import api
from helper.cache import Cache
import RPi.GPIO as GPIO
import locale

pages = (
  ps.start.Start,
  ps.welcome.Welcome,
  ps.fuel_selection.FuelSelection
)

class MainApplication(Tk):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_BUTTON_LEFT_TOP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_BUTTON_LEFT_MIDDLE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_BUTTON_LEFT_BOTTOM, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_BUTTON_RIGHT_TOP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_BUTTON_RIGHT_MIDDLE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_BUTTON_RIGHT_BOTTOM, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    self.title("My GUI App")

    self.container = tk.Frame(self)
    self.container.pack(side = "top", fill="both", expand=True)
    self.container.grid_rowconfigure(0, weight = 1)
    self.container.grid_columnconfigure(0, weight=1)
    self.container.configure(bg=COLOR_BLUE)
    
    self.frames = {} 
      
    self.show_page(ps.start.Start)

  def show_page(self, container, data=None):
    frame = container(self.container, self, data)
    frame.configure(bg=COLOR_BLUE)
    frame.grid(row = 0, column = 0, sticky ="nsew")
    frame.tkraise()
  
  def previous_page(self, container):
    container.destroy()
  
  def get_user_data(self, data):
    return api.get_user_data(data)
  
  def get_data(self, query):
    return api.get(query)
  
  def post_data(self, endpoint, body):
    return api.post(endpoint, body)
  
  def set_cache(self, cache_name, data):
    Cache.save_cache(cache_name, data)
    
  def get_cache(self, cache_name):
    return Cache.get_cache(cache_name)
  
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
    
if __name__ == "__main__":
    app = MainApplication()
    app.configure(bg=COLOR_BLUE)
    # app.geometry("1280x800")
    app.attributes("-fullscreen", True)
    app.wm_title("Welcome to AIOITS")
    app.mainloop()