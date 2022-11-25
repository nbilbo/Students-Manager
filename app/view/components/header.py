import tkinter as tk
import tkinter.ttk as ttk


HEADER_FONT = ('Consolas', 18, 'normal')


class Header(ttk.Frame):
    def __init__(self, master: tk.Misc, text: str) -> None:
        super().__init__(master)

        self.title = ttk.Label(self)
        self.title.configure(font=HEADER_FONT)
        self.title.configure(anchor=tk.CENTER)
        self.title.configure(text=text)
        self.title.pack(side=tk.TOP, fill=tk.X)

    def set_title(self, value: str) -> None:
        self.title.configure(text=value)
