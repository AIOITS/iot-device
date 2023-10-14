from tkinter import *
import tkinter as tk
from config.style import *
from config.constant import *

class ConfirmationTemplate:
    def __init__(self, root, controller):
        self.title = tk.Frame(root)
        self.title.place(relx=0.5, rely=0.06, anchor='n')
        self.title.configure(bg=COLOR_BLUE)
        
        self.content = tk.Frame(root)
        self.content.place(relx=0, rely=0.22, anchor='nw')
        self.content.configure(bg=COLOR_BLUE)
        
        self.instruction = tk.Frame(root)
        self.instruction.place(relx=0.5, rely=0.95, anchor='s')
        self.instruction.configure(bg=COLOR_BLUE)
        
        self.right_bottom = tk.Frame(root)
        self.right_bottom.place(relx=1, rely=0.85, anchor='e')
        self.right_bottom.configure(bg=COLOR_BLUE)
        
        controller.button_listener.clear_onPressed()
        
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