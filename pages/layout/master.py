import tkinter as tk
from tkinter import *
from config.constant import *
from config.style import *

class LayoutMaster:
    def __init__(self, root, controller):
        self.title = tk.Frame(root)
        self.title.place(relx=0, rely=0.15, anchor='w')
        self.title.configure(bg=COLOR_BLUE)
        
        self.left_middle = tk.Frame(root)
        self.left_middle.place(relx=0, rely=0.5, anchor='w')
        self.left_middle.configure(bg=COLOR_BLUE)
        
        self.left_bottom = tk.Frame(root)
        self.left_bottom.place(relx=0, rely=0.85, anchor='w')
        self.left_bottom.configure(bg=COLOR_BLUE)

        self.right_top = tk.Frame(root)
        self.right_top.place(relx=1, rely=0.15, anchor='e')
        self.right_top.configure(bg=COLOR_BLUE)
        
        self.right_middle = tk.Frame(root)
        self.right_middle.place(relx=1, rely=0.5, anchor='e')
        self.right_middle.configure(bg=COLOR_BLUE)
        
        self.right_bottom = tk.Frame(root)
        self.right_bottom.place(relx=1, rely=0.85, anchor='e')
        self.right_bottom.configure(bg=COLOR_BLUE)
        
        controller.button_listener.clear_onPressed()
        
        controller.button_listener.onPressed(PIN_BUTTON_LEFT_BOTTOM, lambda pin: self.invoke(self.left_bottom))
        controller.button_listener.onPressed(PIN_BUTTON_RIGHT_TOP, lambda pin: self.invoke(self.right_top))
        controller.button_listener.onPressed(PIN_BUTTON_RIGHT_MIDDLE, lambda pin: self.invoke(self.right_middle))
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