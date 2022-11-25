import os
import tkinter as tk
# import tkinter.ttk as ttk
import ttkbootstrap as ttk
from app.constants import ICONS_DIR


class Nav(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)

        self.home_icon = tk.PhotoImage(
            file=os.path.join(ICONS_DIR, 'home.png')
        )
        self.home_button = ttk.Button(self)
        self.home_button.configure(text='Home')
        self.home_button.configure(image=self.home_icon, compound=tk.LEFT)
        self.home_button['bootstyle'] = 'outline-default'
        self.home_button.pack(side=tk.LEFT)

        self.students_icon = tk.PhotoImage(
            file=os.path.join(ICONS_DIR, 'students.png')
        )
        self.students_button = ttk.Button(self)
        self.students_button.configure(text='Students')
        self.students_button.configure(
            image=self.students_icon, compound=tk.LEFT
        )
        self.students_button['bootstyle'] = 'outline-default'
        self.students_button.pack(side=tk.LEFT)

        self.about_icon = tk.PhotoImage(
            file=os.path.join(ICONS_DIR, 'about.png')
        )
        self.about_button = ttk.Button(self)
        self.about_button.configure(text='About')
        self.about_button.configure(image=self.about_icon, compound=tk.LEFT)
        self.about_button['bootstyle'] = 'outline-default'
        self.about_button.pack(side=tk.LEFT)
