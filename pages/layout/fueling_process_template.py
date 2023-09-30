import tkinter as tk
from config.style import *
from config.constant import *

class FuelingProcessTemplate:
    def __init__(self, root, controller):
        self.title = tk.Frame(root)
        self.title.place(relx=0.5, rely=0.10, anchor='n')
        self.title.configure(bg=COLOR_BLUE)
        
        content = tk.Frame(root)
        content.place(relx=0.5, rely=0.5, anchor='center')
        content.configure(bg=COLOR_BLUE)
        
        self.progress_bar = tk.Frame(content)
        self.progress_bar.grid(row=0, columnspan=2)
        self.progress_bar.configure(bg=COLOR_WHITE, padx=12, pady=12)
        
        self.price = tk.Frame(content)
        self.price.grid(row=1, column=0, sticky='w')
        self.price.configure(bg=COLOR_BLUE)
        
        self.amount = tk.Frame(content)
        self.amount.grid(row=1, column=1, sticky='e')
        self.amount.configure(bg=COLOR_BLUE)
        
        self.instruction = tk.Frame(root)
        self.instruction.place(relx=0.5, rely=0.95, anchor='s')
        self.instruction.configure(bg=COLOR_BLUE)
        
        self.remaining_balance = tk.Frame(root)
        self.remaining_balance.place(relx=0, rely=0.95, anchor='sw')
        self.remaining_balance.configure(bg=COLOR_BLUE)
        
        controller.clear_onPressed()
        