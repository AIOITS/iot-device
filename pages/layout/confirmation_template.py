import tkinter as tk
from config.style import *
from config.constant import *

class ConfirmationTemplate:
    def __init__(self, root, controller):
        self.title = tk.Frame(root)
        self.title.place(relx=0.5, rely=0.10, anchor='n')
        self.title.configure(bg=COLOR_BLUE)
        
        self.content = tk.Frame(root)
        self.content.place(relx=0, rely=0.2, anchor='nw')
        self.content.configure(bg=COLOR_BLUE)
        
        self.instruction = tk.Frame(root)
        self.instruction.place(relx=0.5, rely=0.95, anchor='s')
        self.instruction.configure(bg=COLOR_BLUE)
        
        self.right_bottom = tk.Frame(root)
        self.right_bottom.place(relx=1, rely=0.85, anchor='e')
        self.right_bottom.configure(bg=COLOR_BLUE)
        
        controller.clear_onPressed()
        
        controller.onPressed(PIN_BUTTON_RIGHT_BOTTOM, lambda pin: self.right_bottom.winfo_children()[0].winfo_children()[-1].invoke())