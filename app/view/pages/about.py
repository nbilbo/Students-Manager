import os
import tkinter as tk
import tkinter.ttk as ttk
from app.constants import IMAGES_DIR
from app.view.components.frame_image import FrameImage
from app.view.components.notepad import Notepad
from app.view.pages.generic import Generic


class About(Generic):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.set_header_title('About')

        notes = [
            'Hi, this is an open-source application.',
            'Fell free to contribue \u270D',
        ]
        self.notepad = Notepad(self.content, notes)
        self.notepad.pack(side=tk.TOP, fill=tk.X)

        self.frame_frame = FrameImage(
            self.content, os.path.join(IMAGES_DIR, 'github.png')
        )
        self.frame_frame.pack(side=tk.TOP, fill=tk.X)
