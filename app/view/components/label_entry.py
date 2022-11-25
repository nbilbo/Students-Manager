import tkinter as tk
import tkinter.ttk as ttk

ENTRY_FONT = ('Serif', 14, 'normal')
LABEL_FONT = ('Serif', 14, 'normal')


class LabelEntry(ttk.Frame):
    def __init__(
        self, master: tk.Misc, text: str, readonly: bool = False
    ) -> None:
        super().__init__(master)
        self.readonly = readonly

        self.label = ttk.Label(self)
        self.label.configure(text=text)
        self.label.configure(anchor=tk.CENTER)
        self.label.configure(font=LABEL_FONT)
        self.label.pack(side=tk.TOP, fill=tk.X)

        self.entry = ttk.Entry(self)
        self.entry.configure(font=ENTRY_FONT)
        self.entry.configure(justify=tk.CENTER)
        self.entry.pack(side=tk.TOP, fill=tk.X)
        if self.readonly:
            self.entry.configure(state=tk.DISABLED)

    def get_value(self) -> str:
        return self.entry.get()

    def set_value(self, value: str) -> None:
        if self.readonly:
            self.entry.configure(state=tk.NORMAL)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, value)

        if self.readonly:
            self.entry.configure(state=tk.DISABLED)
