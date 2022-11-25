import tkinter as tk
import tkinter.ttk as ttk
import typing


TREEVIEW_FONT = ('Serif', 14, 'normal')


class Table(ttk.Frame):
    def __init__(self, master: tk.Misc, columns: typing.List[str]) -> None:
        super().__init__(master)
        self.pack_propagate(False)

        self.treeview = ttk.Treeview(self)
        self.treeview.configure(style='Table.Treeview')
        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.treeview.yview)

        self.treeview.configure(show='headings')
        self.treeview.configure(columns=columns)
        for column in columns:
            self.treeview.heading(column, text=column)
            self.treeview.column(
                column, stretch=True, anchor=tk.CENTER, minwidth=100, width=100
            )

        style = ttk.Style()
        style.configure('Table.Treeview', font=TREEVIEW_FONT, rowheight=40)

    def clear(self) -> None:
        self.treeview.delete(*self.treeview.get_children())

    def insert(self, values: typing.Iterable[str]) -> None:
        self.treeview.insert('', tk.END, values=values)

    def get_selection(self) -> typing.List[typing.List[str]]:
        results = []
        selections = self.treeview.selection()
        for selection in selections:
            values = [
                str(value) for value in self.treeview.item(selection)['values']
            ]
            results.append(values)

        return results
