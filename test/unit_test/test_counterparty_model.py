import pytest
from app.model import Counterparty
from app.db import db


@pytest.fixture(scope='function')
def seed_db_for_testing():
    database = db()
    database.seed_test_db()


def test_fetch_all_counterparty(seed_db_for_testing):
    """
    GIVEN a counterparty mode
    WHEN fetch_all_counterparty method is called
    THEN check
    - it returns a list of tuples,
    - it returns all 5 counterparty,
    - it retruns all 7 columns
    """
    model = Counterparty()
    counterparty_list = model.fetch_all_counterparty()
    assert isinstance(counterparty_list, list)
    for counterparty in counterparty_list:
        assert isinstance(counterparty, tuple)
    assert len(counterparty_list) == 5
    for counterparty in counterparty_list:
        assert len(counterparty) == 7


def test_get_counterparty_by_id(seed_db_for_testing):
    """
    GIVEN a counterparty model
    WHEN get_counterparty_by_id method is called
    THEN check
    - it returns a tuple
    - it retruns the correct data.
    """
    model = Counterparty()
    counterparty = model.get_counterparty_by_id(1)
    assert isinstance(counterparty, tuple)
    assert counterparty[0] == 1
    counterparty = model.get_counterparty_by_id(2)
    assert isinstance(counterparty, tuple)
    assert counterparty[0] == 2
    counterparty = model.get_counterparty_by_id(5)
    assert isinstance(counterparty, tuple)
    assert counterparty[0] == 5


def test_add_new_counterparty(seed_db_for_testing):
    """
    GIVEN a counterparty model
    WHEN get_counterparty_by_id method is called
    THEN check
    - it returns a tuple of the added counterparty,
    - it assigns the correct counterparty_id,
    - it commits the change to database
    """
    new_counterparty = {
        'counterparty_legal_name': 'ORM group',
        'legal_address_id': 4,
        'commercial_contact': 'Hafid',
        'delivery_contact': 'Abdul'
    }
    model = Counterparty()
    added_counterparty = model.add_new_counterparty(new_counterparty)
    added_counterparty_id = added_counterparty[0]
    assert isinstance(added_counterparty, tuple)
    assert added_counterparty_id == 6
    counterparty_list = model.fetch_all_counterparty()
    assert len(counterparty_list) == 6
