from tkinter import *
import tkinter as tk
from config.style import *
import locale
from .layout.master import LayoutMaster
from .component.button import RightButton, LeftButton
from .component.label import CustomLabel, LeftLabel
import pages.init as ps

class FuelSelection(tk.Frame):
  def __init__(self, parent, controller, data):
    tk.Frame.__init__(self, parent)
    self.grid(row = 0, column = 0)
    self.state = {
      "vehicle_index": 0,
      "user_data": controller.get_cache("user-data"),
      "choosen_vehicle": data["choosen_vehicle"],
      "bbm": self.get_bbm_based_on_category(controller.get_cache("bbm"), data["choosen_vehicle"]['bahan_bakar'])
    }
    
    layout = LayoutMaster(root=self)
    
    LeftLabel(
      container=layout.title,
      components=[
        CustomLabel(
          text = "JENIS BBM",
          font = FONT_HEADING_1_BOLD,
        )
      ],
      padx=(PADDING_FROM_FRAME, 0),
    )
    
    LeftButton(
      container=layout.left_bottom,
      components=[
        CustomLabel(
          text ="KEMBALI",
          font = FONT_HEADING_2_BOLD,
        )
      ],
      onClick=lambda: controller.previous_page(self)
    )
    
    self.bbm_handler(layout, controller)
  
  def bbm_handler(self, layout, controller):
    for widget in layout.right_top.winfo_children(): widget.destroy()
    for widget in layout.right_middle.winfo_children(): widget.destroy()
    
    for i in range(len(self.state['bbm'])):
      RightButton(
        container=layout.right_bottom if ((i + 1) % 3 == 0) else layout.right_middle if ((i + 1) % 2 == 0) else layout.right_top,
        onClick=lambda index=i: controller.show_page(ps.fuel_input.FuelInput, {"choosen_vehicle": self.state["choosen_vehicle"], "choosen_bbm": self.state['bbm'][index]}),
        components=[
          CustomLabel(
            text = f"{self.state['bbm'][i]['name']} (subsidi)",
            font = FONT_HEADING_2_BOLD,
          ) if self.state['bbm'][i]['is_subsidi']
          else CustomLabel(
            text = f"{self.state['bbm'][i]['name']}",
            font = FONT_HEADING_2_BOLD,
          ),
          CustomLabel(
            text = self.state['bbm'][i]['type'],
            font = FONT_HEADING_3_REGULAR,
          ),
          CustomLabel(
            text = f"Rp{self.format_money(self.state['bbm'][i]['price_per_liter'])}/Liter",
            font = FONT_HEADING_3_REGULAR,
          ),
        ],
      )
  
  def format_money(self, number):
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
    formatted_number = locale.format_string('%d', number, grouping=True)
    return formatted_number
  
  def get_bbm_based_on_category(self, bbm, category):
    return list(filter(lambda it: it['category'] == category, bbm))