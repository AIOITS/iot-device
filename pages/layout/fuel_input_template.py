import tkinter as tk
from tkinter import *
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
        
        controller.button_listener.clear_onPressed()
        
        controller.button_listener.onPressed(PIN_BUTTON_LEFT_BOTTOM, lambda pin: self.invoke(self.left_bottom))
        controller.button_listener.onPressed(PIN_BUTTON_RIGHT_BOTTOM, lambda pin: self.invoke(self.right_bottom))
        
    def invoke(self, frame):
        button = frame.winfo_children()[0].winfo_children()[-1]
        if (button.winfo_class() == 'Button'): button.invoke()
    
    def create_label(self, container, text, font):
        return Label(
            container,
            fg=COLOR_WHITE,
            bg=COLOR_BLUE,
            text = text,
            font = font,
            relief='flat',
        )