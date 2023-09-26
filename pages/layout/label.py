import tkinter as tk
from tkinter import *
from config.style import *

class CustomLabel:
    def __init__(
        self,
        text,
        font,
        fg=COLOR_WHITE,
        bg=COLOR_BLUE,
    ):
        self.text = text
        self.font = font
        self.fg = fg
        self.bg = bg

class LeftLabel:
    def __init__(self, container, components, row=0, **kwargs):
        frame = tk.Frame(container)
        frame.configure(bg=COLOR_BLUE)
        frame.grid(row=row, sticky='w', **kwargs)
        
        for index, component in enumerate(components):
            Label(
                frame,
                text=component.text,
                font=component.font,
                fg=component.fg,
                bg=component.bg,
                relief='flat',
            ).grid(row=row+index, column=0, sticky='w')
