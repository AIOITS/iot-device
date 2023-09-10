
from tkinter import *
import tkinter as tk
from config.style import *
import pages.init as ps

class Start(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    
    user_data = controller.get_data(
      data='''
        name,
          saldo,
          kuota_subsidi
          ktp{
            stnk{
              nomor_polisi
              merk
              model
            }
          }
        '''
    )
    controller.set_cache("user-data", user_data["data"]["user"][0])
    
    Label(
      self,
      text ="SILAHKAN",
      font = FONT_BODY_REGULAR,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE
    ).place(relx = 0.5, rely = 0.4, anchor = 'center')
    
    Label(
      self,
      text ="TAP KARTU",
      font = FONT_DISPLAY_1_BOLD,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE
    ).place(relx = 0.5, rely = 0.5, anchor = 'center')
    
    Button(
      self,
      text ="Page 2",
      command = lambda : controller.show_page(ps.welcome.Welcome)
    ).place(relx = 0.5, rely = 0.6, anchor = 'center')