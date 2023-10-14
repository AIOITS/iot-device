import tkinter as tk
from config.constant import *
from config.style import *

class AnnouncementLayout:
    def __init__(self, root, controller):
      self.title = tk.Frame(root)
      self.title.place(relx=0, rely=0.15, anchor='w')
      self.title.configure(bg=COLOR_BLUE)
      
      self.content = tk.Frame(root)
      self.content.place(relx=0.5, rely=0.5, anchor='center')
      self.content.configure(bg=COLOR_BLUE)
      
      controller.button_listener.clear_onPressed()