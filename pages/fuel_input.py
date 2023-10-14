from tkinter import *
import tkinter as tk
from config.style import *
import locale
from .layout.fuel_input_template import FuelInputTemplate
from .component.button import RightButton, LeftButton
from .component.label import CustomLabel, LeftLabel, CenterLabel
import pages.init as ps

class FuelInput(tk.Frame):
  def __init__(self, parent, controller, data):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    self.grid(row = 0, column = 0)
    self.state = {
      "vehicle_index": 0,
      "user_data": None,
      "choosen_vehicle": None,
      "choosen_bbm": None,
    }
    
    self.layout = FuelInputTemplate(root=self, controller=controller)
    
    Label(
      self.layout.title,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE,
      bd=0,
      font=FONT_HEADING_3_BOLD,
      text="JUMLAH LITER PENGISIAN",
      relief='flat',
    ).grid(row=0, column=0, sticky="w", padx=(PADDING_FROM_FRAME, 0))
    
    Label(
      self.layout.price_label,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE,
      bd=0,
      font=FONT_HEADING_2_BOLD,
      text="Rp",
      relief='flat',
    ).grid(row=0, column=0, sticky="ew", padx=(0, 16))
    
    self.entry = Entry(
      self.layout.price,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE,
      width=10,
      bd=0,
      highlightbackground=COLOR_BLUE,
      highlightcolor=COLOR_BLUE,
      font=FONT_HEADING_2_BOLD,
      relief='solid',
      justify='center',
    )
    self.entry.focus_set()
    self.entry.grid(row=0, column=1, pady=(0,8))
    self.entry.bind("<KeyRelease>", self.format_and_update_entry)

    
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
    
    self.layout.create_label(
      container = self.layout.right_bottom,
      text = 'SELANJUTNYA',
      font = FONT_HEADING_4_BOLD,
    ).grid(row=0, column=0, sticky='e')
    
    Button(
      self.layout.right_bottom,
      text ="",
      font = FONT_BUTTON_DECORATION,
      fg=COLOR_WHITE,
      bg=COLOR_WHITE,
      width=4,
      relief="flat",
      command=lambda: controller.show_frame(ps.confirmation.Confirmation, {
        "choosen_vehicle": self.state["choosen_vehicle"],
        "choosen_bbm": self.state["choosen_bbm"],
        "expenses": self.get_numeric_value(self.entry.get()),
      })
    ).grid(column=1, row=0, padx=(16, 0))
  
  def update(self, data):
    if (not data): pass
    print(data["choosen_vehicle"])
    self.state = {
      "vehicle_index": 0,
      "user_data": self.controller.get_cache("user-data"),
      "choosen_vehicle": data["choosen_vehicle"],
      "choosen_bbm": data["choosen_bbm"],
    }
  
  def format_money(self, number):
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
    formatted_number = locale.format_string('%d', number, grouping=True)
    return formatted_number
  
  def get_numeric_value(self, input):
    return float(''.join(filter(str.isdigit, input)))
  
  def format_and_update_entry(self, event):
    current_value = self.entry.get()
    numeric_value = ''.join(filter(str.isdigit, current_value))

    try:
        numeric_value = int(numeric_value)
        if (numeric_value > self.state['user_data']['saldo']) : numeric_value = 0
    except ValueError:
        numeric_value = 0

    formatted_value = self.format_money(numeric_value)

    self.entry.delete(0, tk.END)
    self.entry.insert(0, formatted_value)