import tkinter as tk
import tkinter.ttk as ttk
from app.view.components.gender_radio import GenderRadio
from app.view.components.label_combobox import LabelCombobox
from app.view.components.label_entry import LabelEntry

PADDING = 15


class StudentForm(ttk.LabelFrame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.configure(padding=PADDING)
        self.configure(text='Student Form')

        # self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.primary_key = LabelEntry(self, 'Id', True)
        self.primary_key.grid(row=0, column=0, sticky=tk.EW, padx=PADDING)

        self.name = LabelEntry(self, 'Full Name')
        self.name.grid(row=1, column=0, sticky=tk.EW, padx=PADDING)

        self.birthday = LabelEntry(self, 'Date of Birth')
        self.birthday.grid(row=2, column=0, sticky=tk.EW, padx=PADDING)

        self.gender = GenderRadio(self)
        self.gender.grid(row=3, column=0, sticky=tk.EW, padx=PADDING)

        classes = [str(index) for index in range(1, 12)]
        self.classroom = LabelCombobox(self, 'Classroom', classes)
        self.classroom.grid(row=1, column=1, sticky=tk.EW, padx=PADDING)

        self.religion = LabelEntry(self, 'Religion')
        self.religion.grid(row=2, column=1, sticky=tk.EW, padx=PADDING)

        self.skill = LabelEntry(self, 'Skill')
        self.skill.grid(row=3, column=1, sticky=tk.EW, padx=PADDING)

    def get_name(self) -> str:
        return self.name.get_value()

    def set_name(self, value: str) -> None:
        self.name.set_value(value)

    def get_birthday(self) -> str:
        return self.birthday.get_value()

    def set_birthday(self, value: str) -> None:
        self.birthday.set_value(value)

    def get_religion(self) -> str:
        return self.religion.get_value()

    def set_religion(self, value: str) -> None:
        self.religion.set_value(value)

    def get_skill(self) -> str:
        return self.skill.get_value()

    def set_skill(self, value: str) -> None:
        return self.skill.set_value(value)

    def get_gender(self) -> str:
        return self.gender.get_value()

    def set_gender(self, value) -> None:
        self.gender.set_value(value)

    def get_classroom(self) -> str:
        return self.classroom.get_value()

    def set_classroom(self, value: str) -> None:
        self.classroom.set_value(value)

    def get_primary_key(self) -> str:
        return self.primary_key.get_value()

    def set_primary_key(self, value: str) -> str:
        self.primary_key.set_value(value)
