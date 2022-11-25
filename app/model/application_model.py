import sqlite3
import typing


class ApplicationModel(object):
    def __init__(self, db_name: str) -> None:
        """
        Database manager.
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self._create_tables()

    def _create_tables(self) -> None:
        table = """CREATE TABLE IF NOT EXISTS STUDENTS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME CHAR(127) NOT NULL,
            BIRTHDAY CHAR(50) NOT NULL,
            GENDER CHAR(1) NOT NULL,
            CLASSROOM CHAR(50) NOT NULL,
            RELIGION CHAR(127) NOT NULL,
            SKILL CHAR(127) NOT NULL,
            FATHER_NAME CHAR(127) NOT NULL,
            FATHER_OCUPATION CHAR(127) NOT NULL,
            MOTHER_NAME CHAR(127) NOT NULL,
            MOTHER_OCUPATION CHAR(127) NOT NULL
        );"""
        self.connection.execute(table)

    def _student_dict(
        self,
        primary_key: int,
        name: str,
        birthday: str,
        gender: str,
        classroom: str,
        religion: str,
        skill: str,
        father_name: str,
        father_ocupation: str,
        mother_name: str,
        mother_ocupation: str,
    ) -> typing.Dict[str, typing.Any]:
        return {
            'primary_key': primary_key,
            'name': name,
            'birthday': birthday,
            'gender': gender,
            'classroom': classroom,
            'religion': religion,
            'skill': skill,
            'father_name': father_name,
            'father_ocupation': father_ocupation,
            'mother_name': mother_name,
            'mother_ocupation': mother_ocupation,
        }

    def close(self) -> None:
        self.connection.close()

    def create_student(
        self,
        name: str,
        birthday: str,
        gender: str,
        classroom: int,
        religion: str,
        skill: str,
        father_name: str,
        father_ocupation: str,
        mother_name: str,
        mother_ocupation: str,
    ) -> int:
        query = """
        insert into students (
            name, 
            birthday, 
            gender, 
            classroom, 
            religion, 
            skill, 
            father_name, 
            father_ocupation,
            mother_name,
            mother_ocupation
        ) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        values = (
            name,
            birthday,
            gender,
            classroom,
            religion,
            skill,
            father_name,
            father_ocupation,
            mother_name,
            mother_ocupation,
        )
        cursor = self.connection.execute(query, values)
        self.connection.commit()

        return cursor.lastrowid

    def update_student(
        self,
        primary_key: int,
        name: str,
        birthday: str,
        gender: str,
        classroom: int,
        religion: str,
        skill: str,
        father_name: str,
        father_ocupation: str,
        mother_name: str,
        mother_ocupation: str,
    ) -> int:
        query = """
        update students 
            set name = ?,
            birthday = ?,
            gender = ?, 
            classroom =?,
            religion = ?, 
            skill = ?, 
            father_name = ?,
            father_ocupation = ?,
            mother_name = ?,
            mother_ocupation = ?
        where id = ?; 
        """
        values = (
            name,
            birthday,
            gender,
            classroom,
            religion,
            skill,
            father_name,
            father_ocupation,
            mother_name,
            mother_ocupation,
            primary_key,
        )

        cursor = self.connection.execute(query, values)
        self.connection.commit()

        return cursor.rowcount

    def delete_student(self, primary_key: int) -> int:
        query = 'delete from students where id = ?;'
        values = (primary_key,)
        cursor = self.connection.execute(query, values)
        self.connection.commit()

        return cursor.rowcount

    def search_students_by_name(
        self, name: str
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        query = 'select * from students where name like ?;'
        values = (name + '%',)
        cursor = self.connection.execute(query, values)
        results = cursor.fetchall()

        return [self._student_dict(*register) for register in results]

    def search_student_by_pk(
        self, primary_key: int
    ) -> typing.Optional[typing.Dict[str, typing.Any]]:
        query = 'select * from students where id = ?'
        values = (primary_key,)
        cursor = self.connection.execute(query, values)
        result = cursor.fetchone()
        if result:
            return self._student_dict(*result)

        return None
