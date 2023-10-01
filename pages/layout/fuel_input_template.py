import tkinter as tk
from config.style import *
from config.constant import *

class FuelInputTemplate:
    def __init__(self, root, controller):
        self.title = tk.Frame(root)
        self.title.place(relx=0.5, rely=0.15, anchor='n')
        self.title.configure(bg=COLOR_BLUE)
        
        group = tk.Frame(root)
        group.place(relx=0.5, rely=0.45, anchor='n')
        group.configure(bg=COLOR_BLUE)
        
        self.price_label = tk.Frame(group)
        self.price_label.grid(row=0, column=0, pady=(0,8))
        self.price_label.configure(bg=COLOR_BLUE)
        
        self.price = tk.Frame(group)
        self.price.grid(row=0, column=1, sticky="ew", pady=(0,8))
        self.price.configure(bg=COLOR_WHITE)
        
        self.left_bottom = tk.Frame(root)
        self.left_bottom.place(relx=0, rely=0.85, anchor='w')
        self.left_bottom.configure(bg=COLOR_BLUE)
        
        self.right_bottom = tk.Frame(root)
        self.right_bottom.place(relx=1, rely=0.85, anchor='e')
        self.right_bottom.configure(bg=COLOR_BLUE)
        
        controller.clear_onPressed()
        
        controller.onPressed(PIN_BUTTON_LEFT_BOTTOM, lambda pin: self.left_bottom.winfo_children()[0].winfo_children()[-1].invoke())
        controller.onPressed(PIN_BUTTON_RIGHT_BOTTOM, lambda pin: self.right_bottom.winfo_children()[0].winfo_children()[-1].invoke())