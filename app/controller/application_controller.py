import typing
from app.constants import DATABASE_PATH
from app.model.application_model import ApplicationModel

if typing.TYPE_CHECKING:
    from app.view.application import Application


class ApplicationController(object):
    def __init__(self, application: 'Application') -> None:
        """
        Uses the view layer to interact with the user and 
        the model layer to save and read data.
        """
        self.application = application
        self.application_model = ApplicationModel(DATABASE_PATH)

        self.application.nav_home_button.configure(command=self.go_home)
        self.application.nav_students_button.configure(
            command=self.go_students
        )
        self.application.nav_about_button.configure(command=self.go_about)

        self.application.create_student_button.configure(
            command=self.create_student
        )
        self.application.update_student_button.configure(
            command=self.update_student
        )
        self.application.delete_student_buton.configure(
            command=self.delete_student
        )

        self.application.clear_student_button.configure(
            command=self.clear_students_form
        )
        self.application.search_student_button.configure(
            command=self.search_students
        )
        self.application.search_student_entry.bind(
            '<Return>', lambda _: self.search_students()
        )
        self.application.students_treeview.bind(
            '<<TreeviewSelect>>', lambda _: self.auto_fill_students_form()
        )

        self.search_students()
    
    def close(self) -> None:
        self.application_model.close()

    def go_home(self) -> None:
        self.application.go_home()

    def go_students(self) -> None:
        self.application.go_students()

    def go_about(self) -> None:
        self.application.go_about()

    def create_student(self) -> None:
        try:
            form = self.application.get_students_page_form()
            self.application_model.create_student(
                name=form['name'],
                birthday=form['birthday'],
                gender=form['gender'],
                classroom=form['classroom'],
                religion=form['religion'],
                skill=form['skill'],
                father_name=form['father_name'],
                father_ocupation=form['father_ocupation'],
                mother_name=form['mother_name'],
                mother_ocupation=form['mother_ocupation'],
            )
        except Exception as error:
            self.application.show_warning_message(str(error))
        else:
            self.search_students()
            self.application.show_success_message(
                f'Student successfully registered.'
            )

    def update_student(self) -> None:
        form = self.application.get_students_page_form()
        primary_key = form.get('primary_key')
        if primary_key:
            try:
                self.application_model.update_student(
                    primary_key=int(primary_key),
                    name=form['name'],
                    birthday=form['birthday'],
                    gender=form['gender'],
                    classroom=form['classroom'],
                    religion=form['religion'],
                    skill=form['skill'],
                    father_name=form['father_name'],
                    father_ocupation=form['father_ocupation'],
                    mother_name=form['mother_name'],
                    mother_ocupation=form['mother_ocupation'],
                )
            except Exception as error:
                self.application.show_warning_message(str(error))
            else:
                self.search_students()
                self.application.show_success_message(
                    f'Student successfully updated.'
                )

        # primary key not in form.
        else:
            self.application.show_warning_message(
                'Please, first select a student.'
            )

    def delete_student(self) -> None:
        form = self.application.get_students_page_form()
        primary_key = form.get('primary_key')
        if primary_key:
            try:
                self.application_model.delete_student(int(primary_key))
            except Exception as error:
                self.application.show_warning_message(str(error))
            else:
                self.clear_students_form()
                self.search_students()
                self.application.show_success_message(
                    'Student successfully deleted.'
                )
        else:
            self.application.show_warning_message(
                'Please, first slect a student.'
            )

    def search_students(self) -> None:
        self.application.clear_students_table()
        searched = self.application.get_searched_student()

        # searching by student id.
        if searched.isnumeric():
            register = self.application_model.search_student_by_pk(
                int(searched)
            )
            values = (register['primary_key'], register['name'])
            self.application.insert_students_table(values)
        
        # searching by student name.
        else:
            registers = self.application_model.search_students_by_name(
                searched
            )
            for register in registers:
                values = (register['primary_key'], register['name'])
                self.application.insert_students_table(values)

    def auto_fill_students_form(self) -> None:
        # first, we get current selections.
        selections = self.application.get_selection_students()

        # getting student full register.
        if selections:
            selection = selections[0]
            primary_key = int(selection[0])
            register = self.application_model.search_student_by_pk(primary_key)

            # filling the form.
            if register:
                self.application.set_students_page_form(
                    primary_key=register['primary_key'],
                    name=register['name'],
                    birthday=register['birthday'],
                    religion=register['religion'],
                    skill=register['skill'],
                    gender=register['gender'],
                    classroom=register['classroom'],
                    father_name=register['father_name'],
                    father_ocupation=register['father_ocupation'],
                    mother_name=register['mother_name'],
                    mother_ocupation=register['mother_ocupation'],
                )

    def clear_students_form(self) -> None:
        self.application.clear_students_form()
