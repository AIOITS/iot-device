import tkinter as tk
from config.constant import *
from config.style import *
from .master import LayoutMaster

class WelcomeTemplate(LayoutMaster):
    def __init__(self, root, controller):
        LayoutMaster.__init__(self, root, controller)
        
        self.greeting_container = tk.Frame(self.title)
        self.greeting_container.configure(bg=COLOR_BLUE, padx=(f'{PADDING_FROM_FRAME}p', 0))
        self.greeting_container.grid(sticky='w')
        
        self.saldo_container = tk.Frame(self.left_middle)
        self.saldo_container.configure(bg=COLOR_BLUE, padx=(f'{PADDING_FROM_FRAME}p', 0))
        self.saldo_container.grid(sticky='w')
        
        self.right_top_button = tk.Frame(self.right_top)
        self.right_top_button.configure(bg=COLOR_BLUE)
        self.right_top_button.grid(sticky='e')
        
        self.right_middle_button = tk.Frame(self.right_middle)
        self.right_middle_button.configure(bg=COLOR_BLUE)
        self.right_middle_button.grid(sticky='e')
        
        self.right_bottom_button = tk.Frame(self.right_bottom)
        self.right_bottom_button.configure(bg=COLOR_BLUE)
        self.right_bottom_button.grid(sticky='e')