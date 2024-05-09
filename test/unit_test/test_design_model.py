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
    WHEN fetch_all_design method is called
    THEN check
    - it returns a list of tuples,
    - it returns all 5 designs,
    - it retruns all 6 columns
    """
    model = Design()
    design_list = model.fetch_all_design()
    assert isinstance(design_list, list)
    for design in design_list:
        assert isinstance(design, tuple)
    assert len(design_list) == 5
    for design in design_list:
        assert len(design) == 6


def test_get_design_by_id(seed_db_for_testing):
    """
    GIVEN a design model
    WHEN get_design_by_id method is called
    THEN check
    - it returns a tuple
    - it retruns the correct data.
    """
    model = Design()
    design = model.get_design_by_id(1)
    assert isinstance(design, tuple)
    assert design[0] == 1
    design = model.get_design_by_id(2)
    assert isinstance(design, tuple)
    assert design[0] == 2
    design = model.get_design_by_id(5)
    assert isinstance(design, tuple)
    assert design[0] == 5


def test_add_new_design(seed_db_for_testing):
    """
    GIVEN a design model
    WHEN get_design_by_id method is called
    THEN check
    - it returns a tuple of the added design,
    - it assigns the correct design_id,
    - it commits the change to database
    """
    new_design = {
        'design_name': 'apple0006',
        'file_location': '/design/apple',
        'file_name': 'apple006.csv'
    }
    model = Design()
    added_design = model.add_new_design(new_design)
    added_design_id = added_design[0]
    assert isinstance(added_design, tuple)
    assert added_design_id == 6
    design_list = model.fetch_all_design()
    assert len(design_list) == 6
