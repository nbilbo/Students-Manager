import os
import tkinter as tk
import tkinter.ttk as ttk
import typing
from app.constants import ICONS_DIR
from app.view.components.crud_buttons import CrudButtons
from app.view.components.search_bar import SearchBar
from app.view.components.table import Table
from app.view.layouts.parent_form import ParentForm
from app.view.layouts.student_form import StudentForm
from app.view.pages.generic import Generic


class Students(Generic):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.set_header_title('Students')

        self.clear_icon = tk.PhotoImage(
            file=os.path.join(ICONS_DIR, 'clear.png')
        )
        self.clear_button = ttk.Button(self.content)
        self.clear_button.configure(text='Clear')
        self.clear_button.configure(image=self.clear_icon, compound=tk.LEFT)
        self.clear_button.pack(side=tk.TOP, anchor=tk.W)

        panedwindow = ttk.PanedWindow(self.content, orient=tk.HORIZONTAL)
        panedwindow.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

        left_frame = ttk.Frame(panedwindow)
        panedwindow.add(left_frame, weight=2)

        right_frame = ttk.Frame(panedwindow)
        panedwindow.add(right_frame, weight=1)

        self.student_form = StudentForm(left_frame)
        self.student_form.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

        self.parent_form = ParentForm(left_frame)
        self.parent_form.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

        self.crud_buttons = CrudButtons(left_frame)
        self.crud_buttons.pack(side=tk.BOTTOM, fill=tk.X)

        self.search_bar = SearchBar(right_frame)
        self.search_bar.pack(side=tk.TOP, fill=tk.X)

        self.table = Table(right_frame, ['id', 'name'])
        self.table.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

    def clear_table(self) -> None:
        self.table.clear()

    def clear_table_selection(self) -> None:
        self.table.clear_selection()

    def insert_table(self, values: typing.Iterable[str]) -> None:
        self.table.insert(values)

    def get_searched_student(self) -> str:
        return self.search_bar.get_value()

    def get_selection_students(self) -> typing.List[typing.List[str]]:
        return self.table.get_selection()

    def get_student_name(self) -> str:
        return self.student_form.get_name()

    def set_student_name(self, value: str) -> None:
        self.student_form.set_name(value)

    def get_student_birthday(self) -> str:
        return self.student_form.get_birthday()

    def set_student_birthday(self, value: str) -> None:
        self.student_form.set_birthday(value)

    def get_student_religion(self) -> str:
        return self.student_form.get_religion()

    def set_student_religion(self, value) -> None:
        self.student_form.set_religion(value)

    def get_student_skill(self) -> str:
        return self.student_form.get_skill()

    def set_student_skill(self, value: str) -> None:
        self.student_form.set_skill(value)

    def get_student_gender(self) -> str:
        return self.student_form.get_gender()

    def set_student_gender(self, value: str) -> None:
        self.student_form.set_gender(value)

    def get_student_classroom(self) -> str:
        return self.student_form.get_classroom()

    def set_student_classroom(self, value: str) -> None:
        self.student_form.set_classroom(value)

    def get_student_primary_key(self) -> str:
        return self.student_form.get_primary_key()

    def set_student_primary_key(self, value: str) -> None:
        return self.student_form.set_primary_key(value)

    def get_father_name(self) -> str:
        return self.parent_form.get_father_name()

    def set_father_name(self, value: str) -> None:
        self.parent_form.set_father_name(value)

    def get_father_ocupation(self) -> str:
        return self.parent_form.get_father_ocupation()

    def set_father_ocupation(self, value: str) -> None:
        self.parent_form.set_father_ocupation(value)

    def get_mother_name(self) -> str:
        return self.parent_form.get_mother_name()

    def set_mother_name(self, value: str) -> None:
        self.parent_form.set_mother_name(value)

    def get_mother_ocupation(self) -> str:
        return self.parent_form.get_mother_ocupation()

    def set_mother_ocupation(self, value: str) -> None:
        self.parent_form.set_mother_ocupation(value)
