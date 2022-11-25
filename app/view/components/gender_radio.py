import tkinter as tk
import tkinter.ttk as ttk


LABEL_FONT = ('Serif', 14, 'normal')
RADIO_FONT = ('Serif', 14, 'normal')


class GenderRadio(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.label = ttk.Label(self)
        self.label.configure(text='Gender')
        self.label.configure(anchor=tk.CENTER)
        self.label.configure(font=LABEL_FONT)
        self.label.grid(row=0, column=0, columnspan=2, sticky=tk.EW)

        self.radio_var = tk.StringVar()
        self.radio_var.set('m')

        self.male_radio = ttk.Radiobutton(self)
        self.male_radio.configure(value='m')
        self.male_radio.configure(text='Male')
        self.male_radio.configure(variable=self.radio_var)
        self.male_radio.grid(row=1, column=0, sticky=tk.E)

        self.female_radio = ttk.Radiobutton(self)
        self.female_radio.configure(text='Female')
        self.female_radio.configure(value='f')
        self.female_radio.configure(variable=self.radio_var)
        self.female_radio.grid(row=1, column=1, sticky=tk.W)

        style = ttk.Style()
        style.configure('TRadiobutton', font=RADIO_FONT)

    def get_value(self) -> str:
        return self.radio_var.get()

    def set_value(self, value: str) -> str:
        if value == self.male_radio.cget(
            'value'
        ) or value == self.female_radio.cget('value'):
            self.radio_var.set(value)
