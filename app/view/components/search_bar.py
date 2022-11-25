import os
import tkinter as tk
# import tkinter.ttk as ttk
import ttkbootstrap as ttk
from app.constants import ICONS_DIR


ENTRY_FONT = ('Serif', 14, 'normal')


class SearchBar(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)

        self.entry = ttk.Entry(self)
        self.entry.configure(font=ENTRY_FONT)
        self.entry.configure(justify=tk.CENTER)
        self.entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        self.search_icon = tk.PhotoImage(
            file=os.path.join(ICONS_DIR, 'search.png')
        )
        self.button = ttk.Button(self)
        self.button.configure(text='Search')
        self.button.configure(image=self.search_icon, compound=tk.LEFT)
        self.button['bootstyle'] = 'outline-default'
        self.button.pack(side=tk.RIGHT, fill=tk.BOTH)

    def get_value(self) -> str:
        return self.entry.get()
