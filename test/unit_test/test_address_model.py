import pytest
from app.model import Address
from app.db import db


@pytest.fixture(scope='function')
def seed_db_for_testing():
    database = db()
    database.seed_test_db()


def test_fetch_all_address_method(seed_db_for_testing):
    """
    GIVEN a address mode
    WHEN fetch_all_address method is called
    THEN check
    - it returns a list of tuples,
    - it returns all 5 addresses,
    - it retruns all 10 columns
    """
    model = Address()
    Address_list = model.fetch_all_address()
    assert isinstance(Address_list, list)
    for address in Address_list:
        assert isinstance(address, tuple)
    assert len(Address_list) == 5
    for address in Address_list:
        assert len(address) == 10


def test_get_address_by_id(seed_db_for_testing):
    """
    GIVEN a address model
    WHEN get_address_by_id method is called
    THEN check
    - it returns a tuple
    - it retruns the correct data.
    """
    model = Address()
    address = model.get_address_by_id(1)
    assert isinstance(address, tuple)
    assert address[0] == 1
    address = model.get_address_by_id(2)
    assert isinstance(address, tuple)
    assert address[0] == 2
    address = model.get_address_by_id(5)
    assert isinstance(address, tuple)
    assert address[0] == 5


def test_add_new_address(seed_db_for_testing):
    """
    GIVEN a address model
    WHEN get_address_by_id method is called
    THEN check
    - it returns a tuple of the added address,
    - it assigns the correct address_id,
    - it commits the change to database
    """
    new_address = {
        'first_line': '75 Hyde Rd',
        'second_line': 'Alexandara Park',
        'district': 'Greater Manchester',
        'city': 'Manchester',
        'postal_code': 'M15 6EG',
        'country': 'United Kingdom',
        'phone': '01616026753'
    }
    model = Address()
    added_address = model.add_new_address(new_address)
    added_address_id = added_address[0]
    assert isinstance(added_address, tuple)
    assert added_address_id == 6
    address_list = model.fetch_all_address()
    assert len(address_list) == 6
