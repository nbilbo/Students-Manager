import pytest
from app.model.application_model import ApplicationModel


STUDENTS = [
    (
        'Jessica',
        '2000',
        'f',
        '1',
        'christian',
        'no skill',
        'Marcos',
        '',
        'Monica',
        '',
    )
]

UPDATED_STUDENTS = [
    (
        1,
        'Carla Jessica',
        '2000',
        'f',
        '1',
        'christian',
        'no skill',
        'Marcos',
        '',
        'Monica',
        '',
    )
]


@pytest.fixture(scope='module')
def model_in_memory():
    model = ApplicationModel(':memory:')
    yield model
    model.close()


@pytest.mark.parametrize(
    'name, birthday, gender, classroom, religion, skill, '
    'father_name, father_ocupation, mother_name, mother_ocupation',
    STUDENTS,
)
def test_create_student_must_insert_student_register(
    model_in_memory: ApplicationModel,
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
):
    primary_key = model_in_memory.create_student(
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

    assert isinstance(primary_key, int)
    register = model_in_memory.search_student_by_pk(primary_key)
    assert register['name'] == name
    assert register['birthday'] == birthday
    assert register['gender'] == gender
    assert register['classroom'] == classroom
    assert register['religion'] == religion
    assert register['skill'] == skill
    assert register['father_name'] == father_name
    assert register['father_ocupation'] == father_ocupation
    assert register['mother_name'] == mother_name
    assert register['mother_ocupation'] == mother_ocupation


def test_search_students_by_name_must_return_all_registers(
    model_in_memory: ApplicationModel,
):
    registers = model_in_memory.search_students_by_name('')
    assert len(registers) == len(STUDENTS)


def test_search_student_by_pk_must_return_single_register(
    model_in_memory: ApplicationModel,
):
    register = model_in_memory.search_student_by_pk(1)
    assert register is not None


@pytest.mark.parametrize(
    'primary_key, name, birthday, gender, classroom, religion, skill, '
    'father_name, father_ocupation, mother_name, mother_ocupation',
    UPDATED_STUDENTS,
)
def test_update_student_must_update_student_register(
    model_in_memory: ApplicationModel,
    primary_key,
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
):

    rowcount = model_in_memory.update_student(
        primary_key,
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

    assert rowcount == 1
    register = model_in_memory.search_student_by_pk(primary_key)
    assert register['name'] == name
    assert register['birthday'] == birthday
    assert register['gender'] == gender
    assert register['classroom'] == classroom
    assert register['religion'] == religion
    assert register['skill'] == skill
    assert register['father_name'] == father_name
    assert register['father_ocupation'] == father_ocupation
    assert register['mother_name'] == mother_name
    assert register['mother_ocupation'] == mother_ocupation


@pytest.mark.parametrize(
    'primary_key', [index + 1 for index in range(len(STUDENTS))]
)
def test_delete_student_must_delete_register(
    model_in_memory: ApplicationModel, primary_key
):
    rowcount = model_in_memory.delete_student(primary_key)
    assert rowcount == 1
    assert model_in_memory.search_student_by_pk(primary_key) is None


def test_delete_student_must_return_rowcount_zero_if_pk_notexists(
    model_in_memory: ApplicationModel,
):
    rowcount = model_in_memory.delete_student(-999)
    assert rowcount == 0
