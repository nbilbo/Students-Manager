import tkinter as tk
import tkinter.ttk as ttk


FOOTER_FONT = ('Consolas', 10, 'normal')


class Footer(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)

        self.copyright = ttk.Label(self)
        self.copyright.configure(font=FOOTER_FONT)
        self.copyright.configure(
            text='\u00A9 Student Registration 2022 - 2023'
        )
        self.copyright.configure(anchor=tk.CENTER)
        self.copyright.pack(side=tk.TOP, fill=tk.X)
