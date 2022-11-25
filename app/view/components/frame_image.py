import tkinter as tk
import tkinter.ttk as ttk


class FrameImage(ttk.Frame):
    def __init__(self, master: tk.Misc, image_path: str) -> None:
        super().__init__(master)

        self.image = tk.PhotoImage(file=image_path)
        self.label_image = ttk.Label(self)
        self.label_image.configure(image=self.image)
        self.label_image.configure(anchor=tk.CENTER)
        self.label_image.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
