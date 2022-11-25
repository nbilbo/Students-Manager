import tkinter as tk
import tkinter.ttk as ttk
import typing


NOTEPAD_FONT = ('Serif', 18, 'normal')


class Notepad(ttk.Frame):
    def __init__(
        self, master: tk.Misc, notes: typing.Optional[typing.List]
    ) -> None:
        super().__init__(master)

        if notes:
            for note in notes:
                self.add_note(note)

    def add_note(self, value: str) -> None:
        note = ttk.Label(self, text=value)
        note.configure(anchor=tk.CENTER)
        note.configure(font=NOTEPAD_FONT)
        note.pack(side=tk.TOP, fill=tk.X)
