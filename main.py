from tkinter import *
import tkinter as tk
from config.style import *
from config.constant import *
import pages.init as ps
from helper.api import api
from helper.cache import Cache
from helper.keypad import KeypadListener
from helper.nfc_listener import NfcListener
from helper.button import ButtonListener
from helper.pump import Pump
import RPi.GPIO as GPIO
import locale

import netifaces as ni
interface_name = 'eth0'

manifest_page = (
  ps.loading_page.LoadingPage,
  ps.start.Start,
  ps.welcome.Welcome,
  ps.fuel_selection.FuelSelection,
  ps.fuel_input.FuelInput,
  ps.confirmation.Confirmation,
  ps.information.Information,
)

class MainApplication(Tk):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
    
    self.pump_relay = Pump()
    self.nfc_listener = NfcListener()
    self.button_listener = ButtonListener()
    self.keypad_listener = KeypadListener()
    self.mac_address = ni.ifaddresses(interface_name)[ni.AF_LINK][0]['addr']
    
    self.title("My GUI App")

    self.container = tk.Frame(self)
    self.container.pack(side = "top", fill="both", expand=True)
    self.container.grid_rowconfigure(0, weight = 1)
    self.container.grid_columnconfigure(0, weight=1)
    self.container.configure(bg=COLOR_BLUE)
    
    self.frames = {}
    self.stack_frame = []
    
    for F in manifest_page:
      self.frames[F] = F(self.container, self, {})
      self.frames[F].configure(bg=COLOR_BLUE)
      self.frames[F].grid(row = 0, column = 0, sticky ="nsew")
    self.show_frame(ps.start.Start, None)

  def show_page(self, container, data=None):
    frame = container(self.container, self, data)
    frame.configure(bg=COLOR_BLUE)
    frame.grid(row = 0, column = 0, sticky ="nsew")
    frame.tkraise()
    
  def show_frame(self, frame, data=None):
    frame = self.frames[frame]
    self.stack_frame.append(frame)
    frame.tkraise()
    frame.update(data)
  
  def previous_page(self, container):
    container.lower()
    self.stack_frame.pop()
    frame = self.stack_frame[-1]
    frame.update(container.state)
    
  def hide_page(self, container):
    frame = self.frames[container]
    frame.lower()
    
    self.stack_frame.pop()
    current_frame = self.stack_frame[-1]
    current_frame.update(frame.state)
  
  def get_user_data(self, uid, data):
    return api.get_user_data(uid,data)
  
  def get_data(self, query):
    return api.get(query)
  
  def post_data(self, endpoint, body, headers={}):
    return api.post(endpoint, body, headers)
  
  def set_cache(self, cache_name, data):
    Cache.save_cache(cache_name, data)
    
  def get_cache(self, cache_name):
    return Cache.get_cache(cache_name)
    
if __name__ == "__main__":
    app = MainApplication()
    app.configure(bg=COLOR_BLUE)
    # app.geometry("1280x800")
    app.attributes("-fullscreen", True)
    app.wm_title("Welcome to AIOITS")
    app.mainloop()
    app.nfc_listener.stop_listen()
    GPIO.cleanup()