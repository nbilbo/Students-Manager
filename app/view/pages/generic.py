import tkinter as tk
import tkinter.ttk as ttk
from app.view.components.content import Content
from app.view.components.footer import Footer
from app.view.components.header import Header


class Generic(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)

        self.header = Header(self, 'Generic')
        self.header.pack(side=tk.TOP, fill=tk.X)

        self.content = Content(self)
        self.content.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

        self.footer = Footer(self)
        self.footer.pack(side=tk.BOTTOM, fill=tk.X)

    def set_header_title(self, value: str) -> None:
        self.header.set_title(value)
