import pytest
from app.model import Department
from app.db import db


@pytest.fixture(scope='function')
def seed_db_for_testing():
    database = db()
    database.seed_test_db()


def test_fetch_all_department_method(seed_db_for_testing):
    """
    GIVEN a department mode
    WHEN fetch_all_department method is called
    THEN check
    - it returns a list of tuples,
    - it returns all 5 departmentes,
    - it retruns all 10 columns
    """
    model = Department()
    department_list = model.fetch_all_department()
    assert isinstance(department_list, list)
    for department in department_list:
        assert isinstance(department, tuple)
    assert len(department_list) == 5
    for department in department_list:
        assert len(department) == 6


def test_get_department_by_id(seed_db_for_testing):
    """
    GIVEN a department model
    WHEN get_department_by_id method is called
    THEN check
    - it returns a tuple
    - it retruns the correct data.
    """
    model = Department()
    department = model.get_department_by_id(1)
    assert isinstance(department, tuple)
    assert department[0] == 1
    department = model.get_department_by_id(2)
    assert isinstance(department, tuple)
    assert department[0] == 2
    department = model.get_department_by_id(5)
    assert isinstance(department, tuple)
    assert department[0] == 5


def test_add_new_department(seed_db_for_testing):
    """
    GIVEN a department model
    WHEN get_department_by_id method is called
    THEN check
    - it returns a tuple of the added department,
    - it assigns the correct department_id,
    - it commits the change to database
    """
    new_department = {
        'department_name': 'Research and Development',
        'location': 'London',
        'manager': 'Khaled'
    }
    model = Department()
    added_department = model.add_new_department(new_department)
    added_department_id = added_department[0]
    assert isinstance(added_department, tuple)
    assert added_department_id == 6
    department_list = model.fetch_all_department()
    assert len(department_list) == 6
