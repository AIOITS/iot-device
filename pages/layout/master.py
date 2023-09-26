import tkinter as tk
from config.style import *

class LayoutMaster:
    def __init__(self, root):
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