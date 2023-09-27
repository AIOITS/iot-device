import tkinter as tk
from config.style import *

class ConfirmationTemplate:
    def __init__(self, root):
        self.title = tk.Frame(root)
        self.title.place(relx=0.5, rely=0.10, anchor='n')
        self.title.configure(bg=COLOR_BLUE)
        
        self.content = tk.Frame(root)
        self.content.place(relx=0.5, rely=0.2, anchor='n')
        self.content.configure(bg=COLOR_BLUE)
        
        self.instruction = tk.Frame(root)
        self.instruction.place(relx=0.5, rely=0.95, anchor='s')
        self.instruction.configure(bg=COLOR_BLUE)