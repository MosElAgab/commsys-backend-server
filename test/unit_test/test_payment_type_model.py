import pytest
from app.model import PaymentType
from app.db import db


@pytest.fixture(scope='function')
def seed_db_for_testing():
    database = db()
    database.seed_test_db()


def test_fetch_all_payment_type_method(seed_db_for_testing):
    """
    GIVEN a payment_type mode
    WHEN fetch_all_payment_type method is called
    THEN check
    - it returns a list of tuples,
    - it returns all 5 payment_typees,
    - it retruns all 10 columns
    """
    model = PaymentType()
    payment_type_list = model.fetch_all_payment_type()
    assert isinstance(payment_type_list, list)
    for payment_type in payment_type_list:
        assert isinstance(payment_type, tuple)
    assert len(payment_type_list) == 5
    for payment_type in payment_type_list:
        assert len(payment_type) == 4


def test_get_payment_type_by_id(seed_db_for_testing):
    """
    GIVEN a payment_type model
    WHEN get_payment_type_by_id method is called
    THEN check
    - it returns a tuple
    - it retruns the correct data.
    """
    model = PaymentType()
    payment_type = model.get_payment_type_by_id(1)
    assert isinstance(payment_type, tuple)
    assert payment_type[0] == 1
    payment_type = model.get_payment_type_by_id(2)
    assert isinstance(payment_type, tuple)
    assert payment_type[0] == 2
    payment_type = model.get_payment_type_by_id(5)
    assert isinstance(payment_type, tuple)
    assert payment_type[0] == 5


def test_add_new_payment_type(seed_db_for_testing):
    """
    GIVEN a payment_type model
    WHEN get_payment_type_by_id method is called
    THEN check
    - it returns a tuple of the added payment_type,
    - it assigns the correct payment_type_id,
    - it commits the change to database
    """
    new_payment_type = {
        'payment_type_name': 'Solona'
    }
    model = PaymentType()
    added_payment_type = model.add_new_payment_type(new_payment_type)
    added_payment_type_id = added_payment_type[0]
    assert isinstance(added_payment_type, tuple)
    assert added_payment_type_id == 6
    payment_type_list = model.fetch_all_payment_type()
    assert len(payment_type_list) == 6
