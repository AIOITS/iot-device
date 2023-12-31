
from tkinter import *
import tkinter as tk
from config.style import *
from config.constant import *
import pages.init as ps

class Start(tk.Frame):
  def __init__(self, parent, controller, data):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    bbm = controller.get_data(
      query='''
        bbm {
          id
          name
          type
          price_per_liter
          category
          is_subsidi
        }
        '''
    )
    controller.set_cache("bbm", bbm['data']['bbm'])
    
    content = tk.Frame(self)
    content.place(relx=0.5, rely=0.5, anchor='center')
    content.configure(bg=COLOR_BLUE)
    
    Label(
      content,
      text ="SILAHKAN",
      font = FONT_HEADING_3_REGULAR,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE
    ).grid(row=0)
    
    Label(
      content,
      text ="TAP KARTU",
      font = FONT_DISPLAY_1_BOLD,
      fg=COLOR_WHITE,
      bg=COLOR_BLUE
    ).grid(row=1)
    
    # Button(
    #   self,
    #   text ="Page 2",
    #   command = lambda : controller.show_page(ps.welcome.Welcome, {})
    # ).place(relx = 0.5, rely = 0.6, anchor = 'center')
    
    self.after(500, self.onListeningHandler)
    # self.after(500, self.onCardScanned('cc02bb4aac2722'))
  
  def update(self, data=None):
    if not data: pass
    self.after(500, self.onListeningHandler)
   
  def onListeningHandler(self):
    self.controller.nfc_listener.listen(self.onCardScanned)
  
  def onCardScanned(self, uid):
    print(f"LOGGER::CARD SCANNED {uid}")
    self.controller.show_frame(ps.loading_page.LoadingPage)
    self.after(50, lambda: self.retrieve_user_data(self.controller, uid))
  
  def retrieve_user_data(self, controller, uid):
    self.controller.nfc_listener.stop_listen()
    user_data = controller.get_user_data(
      uid=uid,
      data='''
        name,
          saldo,
          ktp{
            stnk{
              nomor_stnk
              nomor_polisi
              kuota_subsidi
              isi_silinder
              merk
              model
              bahan_bakar
              jenis
            }
          }
        '''
    )
    
    user_jwt = controller.post_data('/auth/login-from-device', {
      "deviceId": controller.mac_address,
      "uid": uid
    })
    
    if(not user_data):
      controller.show_frame(ps.information.Information, {"text": 'KARTU ANDA\nTIDAK TERDAFTAR'})
      controller.hide_page(ps.loading_page.LoadingPage)
    else:
      controller.set_cache("user-jwt", user_jwt["data"]["access_token"])
      controller.set_cache("user-data", user_data["data"]["user"][0])
      controller.set_cache("user-uid", uid)
      controller.show_frame(ps.welcome.Welcome, {"uid": uid})
      controller.hide_page(ps.loading_page.LoadingPage)
