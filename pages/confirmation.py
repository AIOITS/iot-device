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
    self.controller = controller
    self.state = {
      "vehicle_index": 0,
      "user_data": None,
      "choosen_vehicle": None,
      "choosen_bbm": None,
      "expenses": 0,
    }
    
    self.layout = ConfirmationTemplate(root=self, controller=controller)
    
    CenterLabel(
      container=self.layout.title,
      components=[
        CustomLabel(
          text = "KONFIRMASI",
          font = FONT_HEADING_3_BOLD,
        )
      ],
      padx=(PADDING_FROM_FRAME, 0),
      pady=(16, 0),
    )
    
    # Kendaraan
    
    self.layout.create_label(
      container = self.layout.content,
      text = 'Kendaraan',
      font = FONT_HEADING_5_REGULAR,
    ).grid(row=0, column=0, rowspan=2, sticky='w', padx=(PADDING_FROM_FRAME, 0))
    
    self.vehicle_information_label = self.layout.create_label(
      container = self.layout.content,
      text = 'Testing',
      font = FONT_HEADING_4_BOLD,
    )
    self.vehicle_information_label.grid(row=0, column=1, sticky='w', padx=(PADDING_FROM_FRAME, 0))
    
    self.vehicle_number_information_label = self.layout.create_label(
      container = self.layout.content,
      text = 'Testing',
      font = FONT_HEADING_5_REGULAR,
    )
    self.vehicle_number_information_label.grid(row=1, column=1, sticky='w', padx=(PADDING_FROM_FRAME, 0))
    
    # Jenis BBM
    
    self.layout.create_label(
      container = self.layout.content,
      text = 'Jenis BBM',
      font = FONT_HEADING_5_REGULAR,
    ).grid(row=2, column=0, sticky='w', padx=(PADDING_FROM_FRAME, 0), pady=(16, 0))
    
    self.bbm_information_label = self.layout.create_label(
      container = self.layout.content,
      text = 'Testing',
      font = FONT_HEADING_4_BOLD,
    )
    self.bbm_information_label.grid(row=2, column=1, sticky='w', padx=(PADDING_FROM_FRAME, 0), pady=(16, 0))
    
    # Skema
    
    self.layout.create_label(
      container = self.layout.content,
      text = 'Skema',
      font = FONT_HEADING_5_REGULAR,
    ).grid(row=3, column=0, sticky='w', padx=(PADDING_FROM_FRAME, 0), pady=(16, 0))
    
    self.schema_information_label = self.layout.create_label(
      container = self.layout.content,
      text = 'Testing',
      font = FONT_HEADING_4_BOLD,
    )
    self.schema_information_label.grid(row=3, column=1, sticky='w', padx=(PADDING_FROM_FRAME, 0), pady=(16, 0))
    
    # Harga/Liter
    
    self.layout.create_label(
      container = self.layout.content,
      text = 'Harga/Liter',
      font = FONT_HEADING_5_REGULAR,
    ).grid(row=4, column=0, sticky='w', padx=(PADDING_FROM_FRAME, 0), pady=(16, 0))
    
    self.price_information_label = self.layout.create_label(
      container = self.layout.content,
      text = 'Testing',
      font = FONT_HEADING_4_BOLD,
    )
    self.price_information_label.grid(row=4, column=1, sticky='w', padx=(PADDING_FROM_FRAME, 0), pady=(16, 0))
    
    # Jumlah
    
    self.layout.create_label(
      container = self.layout.content,
      text = 'Jumlah',
      font = FONT_HEADING_5_REGULAR,
    ).grid(row=5, column=0, sticky='w', padx=(PADDING_FROM_FRAME, 0), pady=(16, 0))
    
    self.amount_information_label = self.layout.create_label(
      container = self.layout.content,
      text = 'Testing',
      font = FONT_HEADING_4_BOLD,
    )
    self.amount_information_label.grid(row=5, column=1, sticky='w', padx=(PADDING_FROM_FRAME, 0), pady=(16, 0))
    
    # Total
    
    self.layout.create_label(
      container = self.layout.content,
      text = 'Total',
      font = FONT_HEADING_5_REGULAR,
    ).grid(row=6, column=0, sticky='w', padx=(PADDING_FROM_FRAME, 0), pady=(16, 0))
    
    self.total_information_label = self.layout.create_label(
      container = self.layout.content,
      text = 'Testing',
      font = FONT_HEADING_4_BOLD,
    )
    self.total_information_label.grid(row=6, column=1, sticky='w', padx=(PADDING_FROM_FRAME, 0), pady=(16, 0))
    
    self.layout.create_label(
      container = self.layout.instruction,
      text = 'Tempel kartu untuk konfirmasi',
      font = FONT_HEADING_5_REGULAR,
    ).grid(row=6, column=0, padx=(PADDING_FROM_FRAME, 0), pady=(16, 0))
    
    
    # Kembali
    
    self.layout.create_label(
      container = self.layout.right_bottom,
      text = 'KEMBALI',
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
      command=lambda: self.onBackButtonClicked()
    ).grid(column=1, row=0, padx=(16, 0))
  
  def update(self, data):
    if (not data): pass
    self.state = {
      "vehicle_index": 0,
      "user_data": self.controller.get_cache("user-data"),
      "choosen_vehicle": data["choosen_vehicle"],
      "choosen_bbm": data["choosen_bbm"],
      "expenses": data["expenses"],
    }
    self.vehicle_information_label.config(text=f"{self.state['choosen_vehicle']['merk']} {self.state['choosen_vehicle']['model']}")
    self.vehicle_number_information_label.config(text=self.state['choosen_vehicle']['nomor_polisi'])
    self.bbm_information_label.config(text=f"{self.state['choosen_bbm']['name']} (subsidi)" if self.state['choosen_bbm']['is_subsidi'] else f"{self.state['choosen_bbm']['name']}")
    self.schema_information_label.config(text="Subsidi" if self.state['choosen_bbm']['is_subsidi'] else "Non Subsidi")
    self.price_information_label.config(text=f"Rp{self.format_money(self.state['choosen_bbm']['price_per_liter'])}/Liter")
    self.amount_information_label.config(text=f"{self.format_decimal(self.state['expenses']/self.state['choosen_bbm']['price_per_liter'])} Liter")
    self.total_information_label.config(text=f"Rp{self.format_money(self.state['expenses'])}")
    self.after(50, lambda: self.controller.nfc_listener.listen(self.onCardScanned))

  def onBackButtonClicked(self):
    self.controller.nfc_listener.stop_listen()
    self.controller.previous_page(self)
  
  def onCardScanned(self, uid):
    print(f"LOGGER::CARD SCANNED {uid}")
    self.controller.show_frame(ps.loading_page.LoadingPage)
    self.after(50, lambda: self.verify_uid(self.controller, uid))
    
  def format_money(self, number):
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
    formatted_number = locale.format_string('%d', number, grouping=True)
    return formatted_number

  def format_decimal(self, number):
    return locale.format_string('%.*f', (2, number), grouping=True)
  
  def change_page(self, controller, page, data=None):
    print(f"LOGGER::Trying to stop Nfc Listener")
    controller.nfc_listener.stop_listen()
    controller.show_page(page, data)
    
  def verify_uid(self, controller, uid):
    user_uid = controller.get_cache("user-uid")
    if (user_uid != uid): return controller.show_page(ps.start.Start)
    data = controller.post_data('/history-pengisian', {
      "kategori_pengisian": "subsidi" if self.state['choosen_bbm']['is_subsidi'] else "non_subsidi",
      "jenis_kendaraan": self.state['choosen_vehicle']['jenis'],
      "jumlah": self.state['expenses']/self.state['choosen_bbm']['price_per_liter'],
      "nomor_stnk": self.state['choosen_vehicle']['nomor_stnk'],
      "bbm_id": int(self.state['choosen_bbm']['id']),
      "device_id": controller.mac_address
    }, {
      "Authorization": f"Bearer {controller.get_cache('user-jwt')}"
    })
    
    if (data['statusCode'] != 201):
      return controller.show_page(ps.confirmation.Confirmation, {
        "choosen_vehicle": self.state["choosen_vehicle"],
        "choosen_bbm": self.state["choosen_bbm"],
        "expenses": self.state["expenses"],
      })
    
    controller.show_page(ps.fueling_process.FuelingProcess, {
      "choosen_vehicle": self.state["choosen_vehicle"],
      "choosen_bbm": self.state["choosen_bbm"],
      "expenses": self.state["expenses"],
      "amount": '{:.3f}'.format(self.state['expenses']/self.state['choosen_bbm']['price_per_liter']),
    })