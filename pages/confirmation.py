from tkinter import *
import tkinter as tk
from config.style import *
import locale
from .layout.confirmation_template import ConfirmationTemplate
from .component.button import RightButton, LeftButton
from .component.label import CustomLabel, LeftLabel, CenterLabel
from.fueling_process import FuelingProcess
class Confirmation(tk.Frame):
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
    }
    
    layout = ConfirmationTemplate(root=self)
    
    CenterLabel(
      container=layout.title,
      components=[
        CustomLabel(
          text = "KONFIRMASI",
          font = FONT_HEADING_1_BOLD,
        )
      ],
      padx=(PADDING_FROM_FRAME, 0),
    )
    
    LeftLabel(
      container=layout.content,
      row=0,
      label= CustomLabel(
            text = "Kendaraan",
            font = FONT_HEADING_3_REGULAR,
          ),
      components=[
        CustomLabel(
          text = f"{self.state['choosen_vehicle']['merk']} {self.state['choosen_vehicle']['model']}",
          font = FONT_HEADING_2_BOLD,
        ),
        CustomLabel(
          text = self.state['choosen_vehicle']['nomor_polisi'],
          font = FONT_HEADING_3_REGULAR,
        )
      ],
    )
    
    LeftLabel(
      container=layout.content,
      row=1,
      label= CustomLabel(
            text = "Jenis BBM",
            font = FONT_HEADING_3_REGULAR,
          ),
      components=[
        CustomLabel(
            text = f"{self.state['choosen_bbm']['name']} (subsidi)",
            font = FONT_HEADING_2_BOLD,
          ) if self.state['choosen_bbm']['is_subsidi']
          else CustomLabel(
            text = f"{self.state['choosen_bbm']['name']}",
            font = FONT_HEADING_2_BOLD,
          ),
      ],
    )
    
    LeftLabel(
      container=layout.content,
      row=2,
      label= CustomLabel(
            text = "Skema",
            font = FONT_HEADING_3_REGULAR,
          ),
      components=[
        CustomLabel(
            text = "Subsidi" if self.state['choosen_bbm']['is_subsidi'] else "Non Subsidi",
            font = FONT_HEADING_2_BOLD,
          )
      ],
    )
    
    LeftLabel(
      container=layout.content,
      row=3,
      label= CustomLabel(
            text = "Harga/Liter",
            font = FONT_HEADING_3_REGULAR,
          ),
      components=[
        CustomLabel(
            text = f"Rp{self.format_money(self.state['choosen_bbm']['price_per_liter'])}/Liter",
            font = FONT_HEADING_2_BOLD,
          )
      ],
    )
    
    LeftLabel(
      container=layout.content,
      row=5,
      label= CustomLabel(
            text = "Jumlah",
            font = FONT_HEADING_3_REGULAR,
          ),
      components=[
        CustomLabel(
            text = f"{'{:.3f}'.format(self.state['expenses']/self.state['choosen_bbm']['price_per_liter'])} Liter",
            font = FONT_HEADING_2_BOLD,
          )
      ],
    )
    
    LeftLabel(
      container=layout.content,
      row=6,
      label= CustomLabel(
            text = "Total",
            font = FONT_HEADING_3_REGULAR,
          ),
      components=[
        CustomLabel(
            text = f"Rp{self.format_money(self.state['expenses'])}",
            font = FONT_HEADING_2_BOLD,
          )
      ],
    )
    
    CenterLabel(
      container=layout.instruction,
      row=7,
      components=[
        CustomLabel(
            text = "Tempel kartu untuk konfirmasi",
            font = FONT_HEADING_3_REGULAR,
          )
      ],
    )
    
    RightButton(
      container=layout.instruction,
      components=[
        CustomLabel(
          text ="SELANJUTNYA",
          font = FONT_HEADING_2_BOLD,
        )
      ],
      onClick=lambda: controller.show_page(FuelingProcess, {
        "choosen_vehicle": self.state["choosen_vehicle"],
        "choosen_bbm": self.state["choosen_bbm"],
        "expenses": self.state["expenses"],
        "amount": '{:.3f}'.format(self.state['expenses']/self.state['choosen_bbm']['price_per_liter']),
      })
    )
  
  def format_money(self, number):
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
    formatted_number = locale.format_string('%d', number, grouping=True)
    return formatted_number