import tkinter as tk
import tkinter.ttk as ttk


PADDING = 15


class Content(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.configure(padding=PADDING)
