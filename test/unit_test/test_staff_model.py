import pytest
from app.model import Staff
from app.db import db


@pytest.fixture(scope='function')
def seed_db_for_testing():
    database = db()
    database.seed_test_db()


def test_fetch_all_staff_method(seed_db_for_testing):
    """
    GIVEN a staff mode
    WHEN fetch_all_staff method is called
    THEN check
    - it returns a list of tuples,
    - it returns all 5 staffes,
    - it retruns all 10 columns
    """
    model = Staff()
    staff_list = model.fetch_all_staff()
    assert isinstance(staff_list, list)
    for staff in staff_list:
        assert isinstance(staff, tuple)
    assert len(staff_list) == 5
    for staff in staff_list:
        assert len(staff) == 7


def test_get_staff_by_id(seed_db_for_testing):
    """
    GIVEN a staff model
    WHEN get_staff_by_id method is called
    THEN check
    - it returns a tuple
    - it retruns the correct data.
    """
    model = Staff()
    staff = model.get_staff_by_id(1)
    assert isinstance(staff, tuple)
    assert staff[0] == 1
    staff = model.get_staff_by_id(2)
    assert isinstance(staff, tuple)
    assert staff[0] == 2
    staff = model.get_staff_by_id(5)
    assert isinstance(staff, tuple)
    assert staff[0] == 5


def test_add_new_staff(seed_db_for_testing):
    """
    GIVEN a staff model
    WHEN get_staff_by_id method is called
    THEN check
    - it returns a tuple of the added staff,
    - it assigns the correct staff_id,
    - it commits the change to database
    """
    new_staff = {
        'first_name': 'Khaled',
        'last_name': 'Abdul',
        'department_id': 2,
        'email_address': 'kahled.abdul@commsys.com'
    }
    model = Staff()
    added_staff = model.add_new_staff(new_staff)
    added_staff_id = added_staff[0]
    assert isinstance(added_staff, tuple)
    assert added_staff_id == 6
    staff_list = model.fetch_all_staff()
    assert len(staff_list) == 6
