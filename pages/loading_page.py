from tkinter import *
import tkinter as tk
from config.style import *
from config.constant import *
from pages.layout.AnnouncementLayout import AnnouncementLayout

class LoadingPage(tk.Frame):
  def __init__(self, parent, controller, data):
    tk.Frame.__init__(self, parent)

    self.grid(row = 0, column = 0)
    
    layout = AnnouncementLayout(root=self, controller=controller)
    
    Label(
      layout.content,
      text = "MOHON TUNGGU",
      font = FONT_HEADING_2_BOLD,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE,
    ).pack()
    
  def update(self):
    pass
    