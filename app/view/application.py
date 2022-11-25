import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import typing
from app.view.components.nav import Nav
from app.controller.application_controller import ApplicationController
from app.view.pages.about import About
from app.view.pages.home import Home
from app.view.pages.students import Students


class Application(tk.Tk):
    def __init__(self) -> None:
        """
        Create all widgets.
        """
        super().__init__()

        # style
        style = ttk.Style()
        style.theme_use('clam')

        style = ttk.Style()
        style.theme_use('clam')
        # widgets.
        self.nav = Nav(self)
        self.nav.pack(side=tk.TOP, fill=tk.X)

        self.pages_container = ttk.Frame(self)
        self.pages_container.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

        self.about = About(self.pages_container)
        self.home = Home(self.pages_container)
        self.students = Students(self.pages_container)

        self.go_students()

    def _clear_pages_container(self) -> None:
        for children in self.pages_container.winfo_children():
            children.pack_forget()

    def go_home(self) -> None:
        self._clear_pages_container()
        self.home.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        self.title('Student Registration')
        self.geometry('1000x650+0+0')

    def go_students(self) -> None:
        self._clear_pages_container()
        self.students.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        self.title('Students Regsitration - Registers')
        self.geometry('1000x650+0+0')

    def go_about(self) -> None:
        self._clear_pages_container()
        self.about.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        self.title('Student Registration - About')
        self.geometry('1000x650+0+0')

    def show_success_message(self, message: str) -> None:
        messagebox.showinfo('Success', message)

    def show_warning_message(self, message: str) -> None:
        messagebox.showwarning('Warning', message)

    def clear_students_table(self) -> None:
        self.students.clear_table()

    def clear_students_form(self) -> None:
        self.set_students_page_form(
            primary_key='',
            name='',
            birthday='',
            religion='',
            skill='',
            gender='m',
            classroom='1',
            father_name='',
            father_ocupation='',
            mother_name='',
            mother_ocupation='',
        )

    def insert_students_table(self, values: typing.Iterable[str]) -> None:
        self.students.insert_table(values)

    def get_searched_student(self) -> str:
        return self.students.get_searched_student()

    def get_selection_students(self) -> typing.List[typing.List[str]]:
        return self.students.get_selection_students()

    def get_students_page_form(self) -> typing.Dict[typing.Any, typing.Any]:
        return {
            # student
            'name': self.students.get_student_name(),
            'birthday': self.students.get_student_birthday(),
            'religion': self.students.get_student_religion(),
            'skill': self.students.get_student_skill(),
            'gender': self.students.get_student_gender(),
            'classroom': self.students.get_student_classroom(),
            'primary_key': self.students.get_student_primary_key(),
            # parent
            'father_name': self.students.get_father_name(),
            'father_ocupation': self.students.get_father_ocupation(),
            'mother_name': self.students.get_mother_name(),
            'mother_ocupation': self.students.get_mother_ocupation(),
        }

    def set_students_page_form(
        self,
        primary_key: str,
        name: str,
        birthday: str,
        religion: str,
        skill: str,
        gender: str,
        classroom: str,
        father_name: str,
        father_ocupation: str,
        mother_name: str,
        mother_ocupation: str,
    ) -> None:
        self.students.set_student_primary_key(primary_key)
        self.students.set_student_name(name)
        self.students.set_student_birthday(birthday)
        self.students.set_student_religion(religion)
        self.students.set_student_gender(gender)
        self.students.set_student_skill(skill)
        self.students.set_student_gender(gender)
        self.students.set_student_classroom(classroom)
        self.students.set_father_name(father_name)
        self.students.set_father_ocupation(father_ocupation)
        self.students.set_mother_name(mother_name)
        self.students.set_mother_ocupation(mother_ocupation)

    @property
    def nav_home_button(self) -> ttk.Button:
        return self.nav.home_button

    @property
    def nav_students_button(self) -> ttk.Button:
        return self.nav.students_button

    @property
    def nav_about_button(self) -> ttk.Button:
        return self.nav.about_button

    @property
    def create_student_button(self) -> ttk.Button:
        return self.students.crud_buttons.create_button

    @property
    def update_student_button(self) -> ttk.Button:
        return self.students.crud_buttons.update_button

    @property
    def delete_student_buton(self) -> ttk.Button:
        return self.students.crud_buttons.delete_button

    @property
    def clear_student_button(self) -> ttk.Button:
        return self.students.clear_button

    @property
    def search_student_button(self) -> ttk.Button:
        return self.students.search_bar.button

    @property
    def search_student_entry(self) -> ttk.Entry:
        return self.students.search_bar.entry

    @property
    def students_treeview(self) -> ttk.Treeview:
        return self.students.table.treeview
