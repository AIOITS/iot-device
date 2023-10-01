from tkinter import *
import tkinter as tk
from config.style import *
from config.constant import *
import locale
from .layout.master import LayoutMaster
from .component.button import RightButton
from .component.label import CustomLabel, LeftLabel
import pages.init as ps

class Welcome(tk.Frame):
  def __init__(self, parent, controller, data):
    tk.Frame.__init__(self, parent)

    self.grid(row = 0, column = 0)
    self.state = {
      "vehicle_index": 0,
      "user_data": controller.get_cache("user-data"),
    }
    
    layout = LayoutMaster(root=self, controller=controller)
    
    LeftLabel(
      container=layout.title,
      components=[
        CustomLabel(
          text ="Selamat Datang",
          font = FONT_HEADING_2_REGULAR,
        ),
        CustomLabel(
          text =self.state['user_data']["name"],
          font = FONT_HEADING_1_BOLD,
        )
      ],
      padx=(PADDING_FROM_FRAME, 0),
    )
    
    LeftLabel(
      container=layout.left_middle,
      components=[
        CustomLabel(
          text ="Saldo",
          font = FONT_HEADING_2_REGULAR,
        ),
        CustomLabel(
          text = f"Rp{Welcome.format_money(self.state['user_data']['saldo'])}",
          font = FONT_HEADING_1_BOLD,
        ),
      ],
      padx=(PADDING_FROM_FRAME, 0),
    )
    
    LeftLabel(
      container=layout.left_bottom,
      components=[
        CustomLabel(
          text ="Sisa Subsidi",
          font = FONT_HEADING_2_REGULAR,
        ),
        CustomLabel(
          text = f"{self.state['user_data']['kuota_subsidi']} Liter",
          font = FONT_HEADING_1_BOLD,
        ),
      ],
      padx=(PADDING_FROM_FRAME, 0),
    )
    
    self.vehicle_handler(layout, controller)
    
    RightButton(
      container=layout.right_bottom,
      components=[
        CustomLabel(
          text ="Kendaraan Selanjutnya",
          font = FONT_HEADING_3_BOLD,
        )
      ],
      onClick=lambda: self.vehicle_handler(layout, controller)
    )
  
  def vehicle_handler(self, layout, controller):
    for widget in layout.right_top.winfo_children(): widget.destroy()
    for widget in layout.right_middle.winfo_children(): widget.destroy() 
    
    for i in range(self.state['vehicle_index'], self.state['vehicle_index']+2):
      if (i < len(self.state['user_data']['ktp']['stnk'])):
        RightButton(
          container=layout.right_top if (i % 2 == 0) else layout.right_middle,
          onClick=lambda index=i: self.choose_vehicle(self.state['user_data']['ktp']['stnk'][index], controller),
          components=[
            CustomLabel(
              text = f"{self.state['user_data']['ktp']['stnk'][i]['merk']} {self.state['user_data']['ktp']['stnk'][i]['model']}",
              font = FONT_HEADING_2_BOLD,
            ),
            CustomLabel(
              text = self.state['user_data']['ktp']['stnk'][i]['nomor_polisi'],
              font = FONT_HEADING_3_REGULAR,
            ),
          ],
        )
        self.state['vehicle_index'] = i + 1
      else:
        self.state['vehicle_index'] = 0
        
  def choose_vehicle(self, vehicle_data, controller):
    controller.show_page(ps.fuel_selection.FuelSelection, {"choosen_vehicle": vehicle_data})

  def format_money(number):
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
    formatted_number = locale.format_string('%d', number, grouping=True)
    return formatted_number