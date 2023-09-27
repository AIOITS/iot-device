from tkinter import *
import tkinter as tk
from config.style import *
import locale
from .layout.fuel_input_template import FuelInputTemplate
from .component.button import RightButton, LeftButton
from .component.label import CustomLabel, LeftLabel, CenterLabel
from .confirmation import Confirmation
class FuelInput(tk.Frame):
  def __init__(self, parent, controller, data):
    tk.Frame.__init__(self, parent)
    self.grid(row = 0, column = 0)
    self.state = {
      "vehicle_index": 0,
      "user_data": controller.get_cache("user-data"),
      "choosen_vehicle": data["choosen_vehicle"],
      "choosen_bbm": data["choosen_bbm"],
    }
    
    layout = FuelInputTemplate(root=self)
    
    CenterLabel(
      container=layout.title,
      components=[
        CustomLabel(
          text = "JUMLAH LITER PENGISIAN",
          font = FONT_HEADING_1_BOLD,
        )
      ],
      padx=(PADDING_FROM_FRAME, 0),
    )
    
    Label(
      layout.price_label,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE,
      bd=0,
      font=FONT_HEADING_1_BOLD,
      text="Rp",
      relief='flat',
    ).grid(row=0, column=0, sticky="ew", padx=(0, 16))
    
    self.entry = Entry(
      layout.price,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE,
      width=10,
      font=FONT_HEADING_1_BOLD,
      relief='flat',
      justify='center',
    )
    self.entry.focus_set()
    self.entry.grid(row=0, column=1, pady=(0,8))
    self.entry.bind("<KeyRelease>", self.format_and_update_entry)

    
    LeftButton(
      container=layout.left_bottom,
      components=[
        CustomLabel(
          text ="KEMBALI",
          font = FONT_HEADING_2_BOLD,
        ),
      ],
      onClick=lambda: controller.previous_page(self)
    )
    
    RightButton(
      container=layout.right_bottom,
      components=[
        CustomLabel(
          text ="SELANJUTNYA",
          font = FONT_HEADING_2_BOLD,
        )
      ],
      onClick=lambda: controller.show_page(Confirmation, {
        "choosen_vehicle": self.state["choosen_vehicle"],
        "choosen_bbm": self.state["choosen_bbm"],
        "expenses": self.get_numeric_value(self.entry.get()),
      })
    )
  
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
    except ValueError:
        numeric_value = 0

    formatted_value = self.format_money(numeric_value)

    self.entry.delete(0, tk.END)
    self.entry.insert(0, formatted_value)
  
  def get_bbm_based_on_category(self, bbm, category):
    return list(filter(lambda it: it['category'] == category, bbm))