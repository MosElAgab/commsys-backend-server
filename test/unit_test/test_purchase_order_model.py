import pytest
from app.model import PurchaseOrder
from app.db import db


@pytest.fixture(scope='function')
def seed_db_for_testing():
    database = db()
    database.seed_test_db()


def test_fetch_all_purchase_order(seed_db_for_testing):
    """
    GIVEN a purchase_order mode
    WHEN fetch_all_purchase_order method is called
    THEN check
    - it returns a list of tuples,
    - it returns all 5 purchase_order,
    - it retruns all 12 columns
    """
    model = PurchaseOrder()
    purchase_order_list = model.fetch_all_purchase_order()
    assert isinstance(purchase_order_list, list)
    for purchase_order in purchase_order_list:
        assert isinstance(purchase_order, tuple)
    assert len(purchase_order_list) == 5
    for purchase_order in purchase_order_list:
        assert len(purchase_order) == 12


def test_get_purchase_order_by_id(seed_db_for_testing):
    """
    GIVEN a purchase_order model
    WHEN get_purchase_order_by_id method is called
    THEN check
    - it returns a tuple
    - it retruns the correct data.
    """
    model = PurchaseOrder()
    purchase_order = model.get_purchase_order_by_id(1)
    assert isinstance(purchase_order, tuple)
    assert purchase_order[0] == 1
    purchase_order = model.get_purchase_order_by_id(2)
    assert isinstance(purchase_order, tuple)
    assert purchase_order[0] == 2
    purchase_order = model.get_purchase_order_by_id(5)
    assert isinstance(purchase_order, tuple)
    assert purchase_order[0] == 5


def test_add_new_purchase_order(seed_db_for_testing):
    """
    GIVEN a purchase_order model
    WHEN get_purchase_order_by_id method is called
    THEN check
    - it returns a tuple of the added purchase_order,
    - it assigns the correct purchase_order_id,
    - it commits the change to database
    """
    new_purchase_order = {
        'staff_id': 2,
        'counterparty_id': 5,
        'item_code': 'RTS232',
        'item_quantity': 4000,
        'item_unit_price': 45,
        'currency_id': 4,
        'agreed_delivery_date': '2025-12-12',
        'agreed_payment_date': '2025-05-01',
        'agreed_delivery_location_id': 1
    }
    model = PurchaseOrder()
    added_purchase_order = model.add_new_purchase_order(new_purchase_order)
    added_purchase_order_id = added_purchase_order[0]
    assert isinstance(added_purchase_order, tuple)
    assert added_purchase_order_id == 6
    purchase_order_list = model.fetch_all_purchase_order()
    assert len(purchase_order_list) == 6
