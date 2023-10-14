from tkinter import *
import tkinter as tk
from config.style import *
from config.constant import *
import locale
from .layout.master import LayoutMaster
from .component.button import RightButton, LeftButton
from .component.label import CustomLabel, LeftLabel
import pages.init as ps

class FuelSelection(tk.Frame):
  def __init__(self, parent, controller, data):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    self.grid(row = 0, column = 0)
    self.state = {
      "vehicle_index": 0,
      "user_data": None,
      "choosen_vehicle": None,
      "bbm": None
    }
    
    self.layout = LayoutMaster(root=self, controller=controller)
    
    self.layout.create_label(
      container = self.layout.title,
      text = 'JENIS BBM',
      font = FONT_HEADING_4_BOLD,
    ).grid(row=1, column=0, sticky='e', padx=(PADDING_FROM_FRAME, 0))
    
    self.layout.create_label(
      container = self.layout.left_bottom,
      text = 'KEMBALI',
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
    
    # First BBM 
    
    self.first_bbm_name = self.layout.create_label(
      container = self.layout.right_top,
      text = 'Testing',
      font = FONT_HEADING_4_BOLD,
    )
    self.first_bbm_name.grid(row=0, column=0, sticky='e')
    
    self.first_bbm_ron = self.layout.create_label(
      container = self.layout.right_top,
      text = 'Testing',
      font = FONT_HEADING_5_REGULAR,
    )
    self.first_bbm_ron.grid(row=1, column=0, sticky='e')
    
    self.first_bbm_number = self.layout.create_label(
      container = self.layout.right_top,
      text = 'Testing',
      font = FONT_HEADING_5_REGULAR,
    )
    self.first_bbm_number.grid(row=2, column=0, sticky='e')
    
    self.first_bbm_button = Button(
      self.layout.right_top,
      text ="",
      font = FONT_BUTTON_DECORATION,
      fg=COLOR_WHITE,
      bg=COLOR_WHITE,
      width=4,
      relief="flat",
    )
    self.first_bbm_button.grid(column=1, row=0, rowspan=3, padx=(16, 0))
    
    # Second BBM 
    
    self.second_bbm_name = self.layout.create_label(
      container = self.layout.right_middle,
      text = 'Testing',
      font = FONT_HEADING_4_BOLD,
    )
    self.second_bbm_name.grid(row=0, column=0, sticky='e')
    
    self.second_bbm_ron = self.layout.create_label(
      container = self.layout.right_middle,
      text = 'Testing',
      font = FONT_HEADING_5_REGULAR,
    )
    self.second_bbm_ron.grid(row=1, column=0, sticky='e')
    
    self.second_bbm_number = self.layout.create_label(
      container = self.layout.right_middle,
      text = 'Testing',
      font = FONT_HEADING_5_REGULAR,
    )
    self.second_bbm_number.grid(row=2, column=0, sticky='e')
    
    self.second_bbm_button = Button(
      self.layout.right_middle,
      text ="",
      font = FONT_BUTTON_DECORATION,
      fg=COLOR_WHITE,
      bg=COLOR_WHITE,
      width=4,
      relief="flat",
    )
    self.second_bbm_button.grid(column=1, row=0, rowspan=3, padx=(16, 0))
    
    # Third BBM 
    
    self.third_bbm_name = self.layout.create_label(
      container = self.layout.right_bottom,
      text = 'Testing',
      font = FONT_HEADING_4_BOLD,
    )
    self.third_bbm_name.grid(row=0, column=0, sticky='e')
    
    self.third_bbm_ron = self.layout.create_label(
      container = self.layout.right_bottom,
      text = 'Testing',
      font = FONT_HEADING_5_REGULAR,
    )
    self.third_bbm_ron.grid(row=1, column=0, sticky='e')
    
    self.third_bbm_number = self.layout.create_label(
      container = self.layout.right_bottom,
      text = 'Testing',
      font = FONT_HEADING_5_REGULAR,
    )
    self.third_bbm_number.grid(row=2, column=0, sticky='e')
    
    self.third_bbm_button = Button(
      self.layout.right_bottom,
      text ="",
      font = FONT_BUTTON_DECORATION,
      fg=COLOR_WHITE,
      bg=COLOR_WHITE,
      width=4,
      relief="flat",
    )
    self.third_bbm_button.grid(column=1, row=0, rowspan=3, padx=(16, 0))
  
  def bbm_handler(self, controller):
    for i in range(len(self.state['bbm'])):
      if ((i + 1) % 3 == 0):
        self.first_bbm_name.config(text=f"{self.state['bbm'][i]['name']} (subsidi)" if self.state['bbm'][i]['is_subsidi'] else f"{self.state['bbm'][i]['name']}")
        self.first_bbm_ron.config(text=self.state['bbm'][i]['type'])
        self.first_bbm_number.config(text=f"Rp{self.format_money(self.state['bbm'][i]['price_per_liter'])}/Liter")
        self.first_bbm_button.config(command=lambda index=i: controller.show_frame(ps.fuel_input.FuelInput, {"choosen_vehicle": self.state["choosen_vehicle"], "choosen_bbm": self.state['bbm'][index]}))
      elif ((i + 1) % 3 == 1):
        self.second_bbm_name.config(text=f"{self.state['bbm'][i]['name']} (subsidi)" if self.state['bbm'][i]['is_subsidi'] else f"{self.state['bbm'][i]['name']}")
        self.second_bbm_ron.config(text=self.state['bbm'][i]['type'])
        self.second_bbm_number.config(text=f"Rp{self.format_money(self.state['bbm'][i]['price_per_liter'])}/Liter")
        self.second_bbm_button.config(command=lambda index=i: controller.show_frame(ps.fuel_input.FuelInput, {"choosen_vehicle": self.state["choosen_vehicle"], "choosen_bbm": self.state['bbm'][index]}))
      else:
        self.third_bbm_name.config(text=f"{self.state['bbm'][i]['name']} (subsidi)" if self.state['bbm'][i]['is_subsidi'] else f"{self.state['bbm'][i]['name']}")
        self.third_bbm_ron.config(text=self.state['bbm'][i]['type'])
        self.third_bbm_number.config(text=f"Rp{self.format_money(self.state['bbm'][i]['price_per_liter'])}/Liter")
        self.third_bbm_button.config(command=lambda index=i: controller.show_frame(ps.fuel_input.FuelInput, {"choosen_vehicle": self.state["choosen_vehicle"], "choosen_bbm": self.state['bbm'][index]}))
      
  def update(self, data):
    if (not data): pass
    self.state = {
      "vehicle_index": 0,
      "user_data": self.controller.get_cache("user-data"),
      "choosen_vehicle": data["choosen_vehicle"],
      "bbm": self.get_bbm_based_on_category(self.controller.get_cache("bbm"), data["choosen_vehicle"]['bahan_bakar'])
    }
    self.bbm_handler(self.controller)
  
  def format_money(self, number):
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
    formatted_number = locale.format_string('%d', number, grouping=True)
    return formatted_number
  
  def get_bbm_based_on_category(self, bbm, category):
    return list(filter(lambda it: it['category'] == category, bbm))