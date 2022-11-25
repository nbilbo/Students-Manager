import tkinter as tk
from app.view.pages.generic import Generic


class Home(Generic):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.set_header_title('Welcome')
