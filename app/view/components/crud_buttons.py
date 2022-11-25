import os
import tkinter as tk
import tkinter.ttk as ttk
from app.constants import ICONS_DIR


CRUD_BUTTONS_FONT = ('Arial', 12, 'normal')


class CrudButtons(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)

        self.create_icon = tk.PhotoImage(
            file=os.path.join(ICONS_DIR, 'create.png')
        )
        self.create_button = ttk.Button(self)
        self.create_button.configure(text='Create')
        self.create_button.configure(style='CrudButtons.TButton')
        self.create_button.configure(image=self.create_icon, compound=tk.LEFT)
        self.create_button.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)

        self.update_icon = tk.PhotoImage(
            file=os.path.join(ICONS_DIR, 'update.png')
        )
        self.update_button = ttk.Button(self)
        self.update_button.configure(text='Update')
        self.update_button.configure(style='CrudButtons.TButton')
        self.update_button.configure(image=self.update_icon, compound=tk.LEFT)
        self.update_button.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)

        self.delete_icon = tk.PhotoImage(
            file=os.path.join(ICONS_DIR, 'delete.png')
        )
        self.delete_button = ttk.Button(self)
        self.delete_button.configure(text='Delete')
        self.delete_button.configure(style='CrudButtons.TButton')
        self.delete_button.configure(image=self.delete_icon, compound=tk.LEFT)
        self.delete_button.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)

        style = ttk.Style()
        style.configure('CrudButtons.TButton', font=CRUD_BUTTONS_FONT)
