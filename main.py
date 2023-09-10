from tkinter import *
import tkinter as tk
from config.style import *
import pages.init as ps
from helper.api import api
from helper.cache import Cache
import time

pages = (
  ps.start.Start,
  ps.welcome.Welcome
)

class MainApplication(Tk):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.title("My GUI App")

    self.container = tk.Frame(self)
    self.container.pack(side = "top", fill="both", expand=True)
    self.container.grid_rowconfigure(0, weight = 1)
    self.container.grid_columnconfigure(0, weight=1)
    self.container.configure(bg=COLOR_BLUE)
    
    self.frames = {} 
    
    for F in pages:
      self.frames[F] = F(self.container, self)
      self.frames[F].configure(bg=COLOR_BLUE)
      self.frames[F].grid(row = 0, column = 0, sticky ="nsew")
    self.show_page(ps.start.Start)

  def show_page(self, container):
    frame = self.frames[container]
    frame.tkraise()
    
  def get_data(self, data):
    return api.get(data)
  
  def post_data(self, endpoint, body):
    return api.post(endpoint, body)
  
  def set_cache(self, cache_name, data):
    Cache.save_cache(cache_name, data)
    
  def get_cache(self, cache_name):
    return Cache.get_cache(cache_name)

if __name__ == "__main__":
    app = MainApplication()
    app.configure(bg=COLOR_BLUE)
    app.geometry("1280x800")
    # app.attributes("-fullscreen", True)
    app.wm_title("Welcome to AIOITS")
    app.mainloop()