from tkinter import *
import tkinter as tk
from tkinter import ttk

from config.style import *
import locale
from .layout.fueling_process_template import FuelingProcessTemplate
from .component.button import RightButton, LeftButton
from .component.label import CustomLabel, LeftLabel, CenterLabel, RightLabel

class FuelingProcess(tk.Frame):
  def __init__(self, parent, controller, data):
    tk.Frame.__init__(self, parent)
    self.grid(row = 0, column = 0)
    print(data)
    self.state = {
      "vehicle_index": 0,
      "user_data": controller.get_cache("user-data"),
      "choosen_vehicle": data["choosen_vehicle"],
      "choosen_bbm": data["choosen_bbm"],
      "expenses": data["expenses"],
      "amount": data["amount"],
    }
    
    self.progress_var = tk.IntVar()
    
    layout = FuelingProcessTemplate(root=self)
    
    self.title = Label(
      layout.title,
      text = "SEDANG MENGISI",
      font = FONT_HEADING_1_BOLD,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE,
    )
    self.title.pack()
    
    LeftLabel(
      container=layout.remaining_balance,
      components=[
        CustomLabel(
          text = "Sisa Saldo",
          font = FONT_HEADING_2_REGULAR,
        ),
        CustomLabel(
          text = "Rp50.000",
          font = FONT_HEADING_1_BOLD,
        )
      ],
      padx=(PADDING_FROM_FRAME, 0),
    )
    
    style = ttk.Style()
    style.theme_use('clam')
    style.configure(
      "Custom.Horizontal.TProgressbar",
      foreground=COLOR_WHITE,
      background=COLOR_WHITE,
      troughcolor=COLOR_BLUE,
      bordercolor=COLOR_WHITE,
      lightcolor=COLOR_WHITE
    )
    
    progress_bar = ttk.Progressbar(layout.progress_bar, orient="horizontal", mode="determinate", variable=self.progress_var, length=1200, maximum=100, style="Custom.Horizontal.TProgressbar")
    progress_bar.grid(row=0, column=1, ipady=24)
    
    self.price = Label(
      layout.price,
      text = f"Rp0 / Rp{self.format_money(self.state['expenses'])}",
      font = FONT_HEADING_2_REGULAR,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE,
    )
    self.price.grid()
    
    self.amount = Label(
      layout.amount,
      text = f"0,00 / {self.state['amount']}",
      font = FONT_HEADING_2_REGULAR,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE,
    )
    self.amount.grid()
    
    self.update_progress()
    
  def format_money(self, number):
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
    formatted_number = locale.format_string('%d', number, grouping=True)
    return formatted_number
  
  def update_progress(self):
    progress_value = self.progress_var.get()
    if progress_value < 100:
      current_value = float(progress_value + 10)
      self.progress_var.set(current_value)
      
      current_price = self.format_money(float('{:.3f}'.format(current_value/100 * float(self.state['expenses']))))
      self.price.config(text=f"Rp{current_price} / Rp{self.format_money(self.state['expenses'])}")
      
      current_amount = '{:.3f}'.format(current_value/100 * float(self.state['amount']))
      self.amount.config(text=f"{current_amount}L / {self.state['amount']}L")
      self.after(300, self.update_progress) 
    else:
      self.title.config(text="SELESAI")