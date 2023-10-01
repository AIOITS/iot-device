from tkinter import *
import tkinter as tk
from config.style import *
import locale
from .layout.confirmation_template import ConfirmationTemplate
from .component.button import RightButton, LeftButton
from .component.label import CustomLabel, LeftLabel, CenterLabel
import pages.init as ps

class Confirmation(tk.Frame):
  def __init__(self, parent, controller, data):
    tk.Frame.__init__(self, parent)
    self.grid(row = 0, column = 0)
    self.state = {
      "vehicle_index": 0,
      "user_data": controller.get_cache("user-data"),
      "choosen_vehicle": data["choosen_vehicle"],
      "choosen_bbm": data["choosen_bbm"],
      "expenses": data["expenses"],
    }
    
    layout = ConfirmationTemplate(root=self, controller=controller)
    
    CenterLabel(
      container=layout.title,
      components=[
        CustomLabel(
          text = "KONFIRMASI",
          font = FONT_HEADING_3_BOLD,
        )
      ],
      padx=(PADDING_FROM_FRAME, 0),
      pady=(16, 0),
    )
    
    LeftLabel(
      container=layout.content,
      row=0,
      label= CustomLabel(
            text = "Kendaraan",
            font = FONT_HEADING_5_REGULAR,
          ),
      components=[
        CustomLabel(
          text = f"{self.state['choosen_vehicle']['merk']} {self.state['choosen_vehicle']['model']}",
          font = FONT_HEADING_4_BOLD,
        ),
        CustomLabel(
          text = self.state['choosen_vehicle']['nomor_polisi'],
          font = FONT_HEADING_5_REGULAR,
        )
      ],
      padx=(PADDING_FROM_FRAME, 0),
      pady=(16, 0),
    ),
    
    LeftLabel(
      container=layout.content,
      row=1,
      label= CustomLabel(
            text = "Jenis BBM",
            font = FONT_HEADING_5_REGULAR,
          ),
      components=[
        CustomLabel(
            text = f"{self.state['choosen_bbm']['name']} (subsidi)",
            font = FONT_HEADING_4_BOLD,
          ) if self.state['choosen_bbm']['is_subsidi']
          else CustomLabel(
            text = f"{self.state['choosen_bbm']['name']}",
            font = FONT_HEADING_4_BOLD,
          ),
      ],
      padx=(PADDING_FROM_FRAME, 0),
      pady=(16, 0),
    )
    
    LeftLabel(
      container=layout.content,
      row=2,
      label= CustomLabel(
            text = "Skema",
            font = FONT_HEADING_5_REGULAR,
          ),
      components=[
        CustomLabel(
            text = "Subsidi" if self.state['choosen_bbm']['is_subsidi'] else "Non Subsidi",
            font = FONT_HEADING_4_BOLD,
          )
      ],
      padx=(PADDING_FROM_FRAME, 0),
      pady=(16, 0),
    ),
    
    LeftLabel(
      container=layout.content,
      row=3,
      label= CustomLabel(
            text = "Harga/Liter",
            font = FONT_HEADING_5_REGULAR,
          ),
      components=[
        CustomLabel(
            text = f"Rp{self.format_money(self.state['choosen_bbm']['price_per_liter'])}/Liter",
            font = FONT_HEADING_4_BOLD,
          )
      ],
      padx=(PADDING_FROM_FRAME, 0),
      pady=(16, 0),
    ),
    
    LeftLabel(
      container=layout.content,
      row=5,
      label= CustomLabel(
            text = "Jumlah",
            font = FONT_HEADING_5_REGULAR,
          ),
      components=[
        CustomLabel(
            text = f"{self.format_decimal(self.state['expenses']/self.state['choosen_bbm']['price_per_liter'])} Liter",
            font = FONT_HEADING_4_BOLD,
          )
      ],
      padx=(PADDING_FROM_FRAME, 0),
      pady=(16, 0),
    ),
    
    LeftLabel(
      container=layout.content,
      row=6,
      label= CustomLabel(
            text = "Total",
            font = FONT_HEADING_5_REGULAR,
          ),
      components=[
        CustomLabel(
            text = f"Rp{self.format_money(self.state['expenses'])}",
            font = FONT_HEADING_4_BOLD,
          )
      ],
      padx=(PADDING_FROM_FRAME, 0),
      pady=(16, 0),
    ),
    
    CenterLabel(
      container=layout.instruction,
      row=7,
      components=[
        CustomLabel(
            text = "Tempel kartu untuk konfirmasi",
            font = FONT_HEADING_5_REGULAR,
          )
      ],
    )
    
    RightButton(
      container=layout.right_bottom,
      components=[
        CustomLabel(
          text ="KEMBALI",
          font = FONT_HEADING_4_BOLD,
        )
      ],
      onClick=lambda: self.change_page(controller, ps.fuel_input.FuelInput, {
      "choosen_vehicle": self.state["choosen_vehicle"],
      "choosen_bbm": self.state["choosen_bbm"],
    })
    )
    
    self.after(1000, lambda: controller.nfc_listener.listen(lambda uid: self.verify_uid(controller, uid)))
  
  def format_money(self, number):
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
    formatted_number = locale.format_string('%d', number, grouping=True)
    return formatted_number

  def format_decimal(self, number):
    return locale.format_string('%.*f', (2, number), grouping=True)
  
  def change_page(self, controller, page, data=None):
    controller.nfc_listener.stop_listen()
    controller.show_page(page, data)
    
  def verify_uid(self, controller, uid):
    user_uid = controller.get_cache("user-uid")
    if (user_uid != uid): return controller.show_page(ps.start.Start)
    
    controller.show_page(ps.fueling_process.FuelingProcess, {
      "choosen_vehicle": self.state["choosen_vehicle"],
      "choosen_bbm": self.state["choosen_bbm"],
      "expenses": self.state["expenses"],
      "amount": '{:.3f}'.format(self.state['expenses']/self.state['choosen_bbm']['price_per_liter']),
    })