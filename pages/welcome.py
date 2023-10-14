from tkinter import *
import tkinter as tk
from config.style import *
from config.constant import *
import locale
from .layout.welcome_template import WelcomeTemplate
from .component.button import RightButton
from .component.label import CustomLabel, LeftLabel
import pages.init as ps

class Welcome(tk.Frame):
  def __init__(self, parent, controller, data):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    self.grid(row = 0, column = 0)
    self.state = {
      "vehicle_index": 0,
      "user_data": None,
    }
    
    self.layout = WelcomeTemplate(root=self, controller=controller)
    
    Label(
      self.layout.greeting_container,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE,
      text ="Selamat Datang",
      font = FONT_HEADING_4_REGULAR,
      relief='flat',
      anchor='w'
    ).pack(anchor='w')
    
    self.name_container = Label(
      self.layout.greeting_container,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE,
      text ='',
      font = FONT_HEADING_3_BOLD,
      relief='flat',
    )
    self.name_container.pack(anchor='w')
    
    Label(
      self.layout.saldo_container,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE,
      text ="Saldo",
      font = FONT_HEADING_4_REGULAR,
      relief='flat',
      anchor='w'
    ).pack(anchor='w')
    
    self.saldo_container = Label(
      self.layout.saldo_container,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE,
      text ='',
      font = FONT_HEADING_3_BOLD,
      relief='flat',
    )
    self.saldo_container.pack(anchor='w')
    
    self.layout.create_label(
      container = self.layout.left_bottom,
      text = 'KELUAR',
      font = FONT_HEADING_4_BOLD,
    ).grid(row=0, column=1, sticky='e')
    
    Button(
      self.layout.left_bottom,
      text ="",
      font = FONT_BUTTON_DECORATION,
      fg=COLOR_WHITE,
      bg=COLOR_WHITE,
      width=4,
      relief="flat",
      command=lambda: controller.previous_page(self)
    ).grid(column=0, row=0, padx=(0, 16))
    
    # First Vehicle 
    
    self.first_vehicle_name = self.layout.create_label(
      container = self.layout.right_top_button,
      text = 'Testing',
      font = FONT_HEADING_4_BOLD,
    )
    self.first_vehicle_name.grid(row=0, column=0, sticky='e')
    
    self.first_vehicle_number = self.layout.create_label(
      container = self.layout.right_top_button,
      text = 'Testing',
      font = FONT_HEADING_5_REGULAR,
    )
    self.first_vehicle_number.grid(row=1, column=0, sticky='e')
    
    self.first_vehicle_button = Button(
      self.layout.right_top_button,
      text ="",
      font = FONT_BUTTON_DECORATION,
      fg=COLOR_WHITE,
      bg=COLOR_WHITE,
      width=4,
      relief="flat",
    )
    self.first_vehicle_button.grid(column=1, row=0, rowspan=2, padx=(16, 0))
    
    # Second Vehicle 
    
    self.second_vehicle_name = self.layout.create_label(
      container = self.layout.right_middle_button,
      text = 'Testing',
      font = FONT_HEADING_4_BOLD,
    )
    self.second_vehicle_name.grid(row=0, column=0, sticky='e')
    
    self.second_vehicle_number = self.layout.create_label(
      container = self.layout.right_middle_button,
      text = 'Testing',
      font = FONT_HEADING_5_REGULAR,
    )
    self.second_vehicle_number.grid(row=1, column=0, sticky='e')
    
    self.second_vehicle_button = Button(
      self.layout.right_middle_button,
      text ="",
      font = FONT_BUTTON_DECORATION,
      fg=COLOR_WHITE,
      bg=COLOR_WHITE,
      width=4,
      relief="flat",
    )
    self.second_vehicle_button.grid(column=1, row=0, rowspan=2, padx=(16, 0))
    
    # Next vehicle button
    
    self.layout.create_label(
      container = self.layout.right_bottom_button,
      text = 'Testing',
      font = FONT_HEADING_4_BOLD,
    ).grid(row=1, column=0, sticky='e')
    
    self.next_vehicle_button = Button(
      self.layout.right_bottom_button,
      text ="",
      font = FONT_BUTTON_DECORATION,
      fg=COLOR_WHITE,
      bg=COLOR_WHITE,
      width=4,
      relief="flat",
      command=lambda: self.vehicle_handler(self.layout, controller)
    )
    self.next_vehicle_button.grid(column=1, row=0, rowspan=2, padx=(16, 0))
    
  def update(self, data):
    if (not data): pass
    self.state = {
      "vehicle_index": 0,
      "user_data": self.controller.get_cache("user-data"),
    }
    self.name_container.config(text=self.state['user_data']['name'])
    self.saldo_container.config(text=f"Rp{Welcome.format_money(self.state['user_data']['saldo'])}")
    self.next_vehicle_button.config(command=lambda: self.vehicle_handler(self.layout, self.controller))
    self.vehicle_handler(self.layout, self.controller)
    
  def vehicle_handler(self, layout, controller):    
    self.first_vehicle_name.config(text='')
    self.first_vehicle_number.config(text='')
    self.first_vehicle_button.grid_forget()
    
    self.second_vehicle_name.config(text='')
    self.second_vehicle_number.config(text='')
    self.second_vehicle_button.grid_forget()
    
    for i in range(self.state['vehicle_index'], self.state['vehicle_index']+2):
      if (i < len(self.state['user_data']['ktp']['stnk'])):
        if (i % 2 == 0):
          self.first_vehicle_name.config(text=f"{self.state['user_data']['ktp']['stnk'][i]['merk']} {self.state['user_data']['ktp']['stnk'][i]['model']}")
          self.first_vehicle_number.config(text=self.state['user_data']['ktp']['stnk'][i]['nomor_polisi'])
          self.first_vehicle_button.grid(column=1, row=0, rowspan=2, padx=(16, 0))
          self.first_vehicle_button.config(command=lambda index=i: self.choose_vehicle(self.state['user_data']['ktp']['stnk'][index], controller))
        else:
          self.second_vehicle_name.config(text=f"{self.state['user_data']['ktp']['stnk'][i]['merk']} {self.state['user_data']['ktp']['stnk'][i]['model']}")
          self.second_vehicle_number.config(text=self.state['user_data']['ktp']['stnk'][i]['nomor_polisi'])
          self.second_vehicle_button.grid(column=1, row=0, rowspan=2, padx=(16, 0))
          self.second_vehicle_button.config(command=lambda index=i: self.choose_vehicle(self.state['user_data']['ktp']['stnk'][index], controller))
        
        self.state['vehicle_index'] = i + 1
      else:
        self.state['vehicle_index'] = 0
        
  def choose_vehicle(self, vehicle_data, controller):
    controller.show_frame(ps.fuel_selection.FuelSelection, {"choosen_vehicle": vehicle_data})

  def format_money(number):
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
    formatted_number = locale.format_string('%d', number, grouping=True)
    return formatted_number
  
  def format_decimal(self, number):
    return locale.format_string('%.*f', (2, number), grouping=True)