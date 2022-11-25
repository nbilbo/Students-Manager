import tkinter as tk
import tkinter.ttk as ttk
import typing


LABEL_FONT = ('Serif', 14, 'normal')
COMBOBOX_FONT = ('Serif', 14, 'normal')


class LabelCombobox(ttk.Frame):
    def __init__(
        self, master: tk.Misc, text: str, values: typing.List[str]
    ) -> None:
        super().__init__(master)

        self.label = ttk.Label(self)
        self.label.configure(anchor=tk.CENTER)
        self.label.configure(text=text)
        self.label.configure(font=LABEL_FONT)
        self.label.pack(side=tk.TOP, fill=tk.X)

        self.combobox = ttk.Combobox(self)
        self.combobox.configure(font=COMBOBOX_FONT)
        self.combobox.configure(justify=tk.CENTER)
        self.combobox.configure(values=values)
        self.combobox.set(values[0])
        self.combobox.pack(side=tk.TOP, fill=tk.X)

    def get_value(self) -> str:
        return self.combobox.get()

    def set_value(self, value: str) -> None:
        self.combobox.set(value)
