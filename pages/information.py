from tkinter import *
import tkinter as tk
from config.style import *
from config.constant import *
from pages.layout.AnnouncementLayout import AnnouncementLayout

class Information(tk.Frame):
  def __init__(self, parent, controller, data):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    self.grid(row = 0, column = 0)
    
    layout = AnnouncementLayout(root=self, controller=controller)
    
    self.information = Label(
      layout.content,
      text = "Testing",
      font = FONT_HEADING_2_BOLD,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE,
    )
    self.information.pack()
    
  def update(self, data):
    if not data['text']: pass
    self.information.config(text=data['text'])
    self.after(3000, lambda: self.controller.previous_page(self))
    
