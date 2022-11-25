import tkinter as tk
import tkinter.ttk as ttk
from app.view.components.label_entry import LabelEntry


PADDING = 15


class ParentForm(ttk.LabelFrame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.configure(padding=PADDING)
        self.configure(text="Parent's Form")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.father_name = LabelEntry(self, "Father's Name")
        self.father_name.grid(row=0, column=0, sticky=tk.EW, padx=PADDING)

        self.father_ocupation = LabelEntry(self, "Father's Ocupation")
        self.father_ocupation.grid(row=1, column=0, sticky=tk.EW, padx=PADDING)

        self.mother_name = LabelEntry(self, "Mother's Name")
        self.mother_name.grid(row=0, column=1, sticky=tk.EW, padx=PADDING)

        self.mother_ocupation = LabelEntry(self, "Mother's Ocupation")
        self.mother_ocupation.grid(row=1, column=1, sticky=tk.EW, padx=PADDING)

    def get_father_name(self) -> str:
        return self.father_name.get_value()

    def set_father_name(self, value: str) -> None:
        self.father_name.set_value(value)

    def get_father_ocupation(self) -> str:
        return self.father_ocupation.get_value()

    def set_father_ocupation(self, value: str) -> None:
        self.father_ocupation.set_value(value)

    def get_mother_name(self) -> str:
        return self.mother_name.get_value()

    def set_mother_name(self, value: str) -> None:
        self.mother_name.set_value(value)

    def get_mother_ocupation(self) -> str:
        return self.mother_ocupation.get_value()

    def set_mother_ocupation(self, value: str) -> None:
        self.mother_ocupation.set_value(value)
