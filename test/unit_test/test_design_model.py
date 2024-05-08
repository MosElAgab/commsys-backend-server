import pytest
from app.model import Design
from app.db import db

@pytest.fixture(scope='function')
def seed_db_for_testing():
    database = db()
    database.seed_test_db()


def test_fetch_all_design_method(seed_db_for_testing):
    """
    GIVEN a design model
    WHEN fetch_all_design method called
    THEN check it retruns the correct a list of tuples,
        it retruns all 5 designs,
        it retruns all 6 columns
    """
    model = Design()
    design_list = model.fetch_all_design()
    assert isinstance(design_list, list)
    for design in design_list:
        assert isinstance(design, tuple)
    assert len(design_list) == 5
    for design in design_list:
        assert len(design) == 6
