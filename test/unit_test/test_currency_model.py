import pytest
from app.model import Currency
from app.db import db


@pytest.fixture(scope='function')
def seed_db_for_testing():
    database = db()
    database.seed_test_db()


def test_fetch_all_currency_method(seed_db_for_testing):
    """
    GIVEN a currency mode
    WHEN fetch_all_currency method is called
    THEN check
    - it returns a list of tuples,
    - it returns all 5 currencyes,
    - it retruns all 10 columns
    """
    model = Currency()
    currency_list = model.fetch_all_currency()
    assert isinstance(currency_list, list)
    for currency in currency_list:
        assert isinstance(currency, tuple)
    assert len(currency_list) == 5
    for currency in currency_list:
        assert len(currency) == 4


def test_get_currency_by_id(seed_db_for_testing):
    """
    GIVEN a currency model
    WHEN get_currency_by_id method is called
    THEN check
    - it returns a tuple
    - it retruns the correct data.
    """
    model = Currency()
    currency = model.get_currency_by_id(1)
    assert isinstance(currency, tuple)
    assert currency[0] == 1
    currency = model.get_currency_by_id(2)
    assert isinstance(currency, tuple)
    assert currency[0] == 2
    currency = model.get_currency_by_id(5)
    assert isinstance(currency, tuple)
    assert currency[0] == 5


def test_add_new_currency(seed_db_for_testing):
    """
    GIVEN a currency model
    WHEN get_currency_by_id method is called
    THEN check
    - it returns a tuple of the added currency,
    - it assigns the correct currency_id,
    - it commits the change to database
    """
    new_currency = {
        'currency_code': 'XRP'
    }
    model = Currency()
    added_currency = model.add_new_currency(new_currency)
    added_currency_id = added_currency[0]
    assert isinstance(added_currency, tuple)
    assert added_currency_id == 6
    currency_list = model.fetch_all_currency()
    assert len(currency_list) == 6
