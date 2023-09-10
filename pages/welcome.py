
from tkinter import *
import tkinter as tk
from config.style import *
import locale

class Welcome(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.grid(row = 0, column = 0)
    
    user_data = controller.get_cache("user-data")
    
    group = tk.Frame(self)
    group.place(relx = 0.5, rely = 0.12, anchor = 'center')
    
    Label(
      group,
      text ="Selamat Datang",
      font = FONT_HEADING_2_REGULAR,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE
    ).grid(row=0, sticky="ew")
    
    Label(
      group,
      text =user_data["name"],
      font = FONT_HEADING_1_BOLD,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE
    ).grid(row=1, sticky="ew")
    
    Label(
      group,
      text = "Silahkan pilih kendaraan yang akan diisi",
      font = FONT_BODY_REGULAR,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE
    ).grid(row=2)
    
    
    left_menu_container = tk.Frame(self)
    left_menu_container.place(relx = 0, rely = 0.96, anchor = 'sw')
    left_menu_container.configure(bg=COLOR_BLUE)
    
    Welcome.create_left_menu(
      row=0,
      parent=left_menu_container,
      name= "Saldo",
      value=f"Rp{Welcome.format_money(user_data['saldo'])}"
    )
    
    Welcome.create_left_menu(
      row=1,
      parent=left_menu_container,
      name= "Sisa Subsidi",
      value=f"{user_data['kuota_subsidi']} Liter"
    )
    
    left_menu_frame = tk.Frame(left_menu_container)
    left_menu_frame.configure(bg=COLOR_BLUE)
    left_menu_frame.grid(row=2, sticky='w')
    
    Label(
      left_menu_frame,
      text ="KELUAR",
      font = FONT_HEADING_2_BOLD,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE
    ).grid(row=0, column=1, sticky='w')
    
    Button(
      left_menu_frame,
      text ="",
      font = FONT_BUTTON_DECORATION,
      fg=COLOR_WHITE,
      bg=COLOR_WHITE,
      width=4,
    ).grid(row=0, column=0, sticky='w', padx=(0, 16))
    
    right_menu_container = tk.Frame(self)
    right_menu_container.place(relx = 1, rely = 0.96, anchor = 'se')
    right_menu_container.configure(bg=COLOR_BLUE)
    
    
    Welcome.create_vehicle_menu(
      row=0,
      parent=right_menu_container,
      name=f"{user_data['ktp']['stnk'][0]['merk']} {user_data['ktp']['stnk'][0]['model']}",
      licence_number=user_data['ktp']['stnk'][0]['nomor_polisi']
    )
    
    Welcome.create_vehicle_menu(
      row=1,
      parent=right_menu_container,
      name=f"{user_data['ktp']['stnk'][0]['merk']} {user_data['ktp']['stnk'][0]['model']}",
      licence_number=user_data['ktp']['stnk'][0]['nomor_polisi']
    )
    
    right_menu_frame = tk.Frame(right_menu_container)
    right_menu_frame.configure(bg=COLOR_BLUE)
    right_menu_frame.grid(row=2, sticky='e')
    
    Label(
      right_menu_frame,
      text ="KENDARAAN SELANJUTNYA",
      font = FONT_HEADING_3_BOLD,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE
    ).grid(row=0, column=0, sticky='e')
    
    Button(
      right_menu_frame,
      text ="",
      font = FONT_BUTTON_DECORATION,
      fg=COLOR_WHITE,
      bg=COLOR_WHITE,
      width=4,
    ).grid(row=0, column=1, sticky='e', padx=(16, 0))
    
  def create_vehicle_menu(parent, name, licence_number, row):
    frame = tk.Frame(parent)
    frame.configure(bg=COLOR_BLUE)
    frame.grid(row=row, sticky='e', pady=(0, DISTANCE_BETWEEN_MENU))
    
    Label(
      frame,
      text = name,
      font = FONT_HEADING_2_BOLD,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE
    ).grid(row=0, sticky='e')
    
    Label(
      frame,
      text = licence_number,
      font = FONT_HEADING_3_REGULAR,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE,
    ).grid(row=1, column=0, sticky='e')
    
    Button(
      frame,
      text ="",
      font = FONT_BUTTON_DECORATION,
      fg=COLOR_WHITE,
      bg=COLOR_WHITE,
      width=4,
    ).grid(row=0, column=1, rowspan=2, sticky='e', padx=(16, 0))
    
  def create_left_menu(parent, name, value, row):
    frame = tk.Frame(parent)
    frame.configure(bg=COLOR_BLUE)
    frame.grid(row=row, sticky='w', pady=(0, DISTANCE_BETWEEN_MENU_SMALL), padx=(64, 0))
    
    Label(
      frame,
      text = name,
      font = FONT_HEADING_2_REGULAR,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE
    ).grid(row=0, sticky='w')
    
    Label(
      frame,
      text = value,
      font = FONT_HEADING_1_BOLD,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE,
    ).grid(row=1, column=0, sticky='w')

  def format_money(number):
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
    formatted_number = locale.format_string('%d', number, grouping=True)
    return formatted_number