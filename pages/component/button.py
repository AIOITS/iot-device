import tkinter as tk
from tkinter import *
from config.style import *

class LeftButton:
    def __init__(self, container, components, onClick=None, row=0):
        frame = tk.Frame(container)
        frame.configure(bg=COLOR_BLUE)
        frame.grid(row=row, sticky='w')
        
        for index, component in enumerate(components):
            Label(
                frame,
                text=component.text,
                font=component.font,
                fg=component.fg,
                bg=component.bg,
                padx=0,
                pady=0,
                borderwidth=0,
                relief='flat',
            ).grid(row=index, column=1, sticky='w')
        
        Button(
            frame,
            text ="",
            font = FONT_BUTTON_DECORATION,
            fg=COLOR_WHITE,
            bg=COLOR_WHITE,
            width=4,
            relief="flat",
            command=onClick
        ).grid(row=0, column=0, rowspan=len(components), sticky='w', padx=(0, 16))

class RightButton:
    def __init__(self, container, components, onClick=None):
        frame = tk.Frame(container)
        frame.configure(bg=COLOR_BLUE)
        frame.grid(row=2, sticky='w')
        
        for index, component in enumerate(components):
            Label(
                frame,
                text=component.text,
                font=component.font,
                fg=component.fg,
                bg=component.bg,
                relief='flat',
            ).grid(row=index, column=0, sticky='e')
        
        Button(
            frame,
            text ="",
            font = FONT_BUTTON_DECORATION,
            fg=COLOR_WHITE,
            bg=COLOR_WHITE,
            width=4,
            relief="flat",
            command=onClick
        ).grid(row=0, column=1, rowspan=len(components), sticky='e', padx=(16, 0))