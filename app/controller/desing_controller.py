from flask import request
from app.model import Design



def get_designs():
    model = Design()
    return model.fetch_all_design(), 200


def get_design_by_id(id):
    model = Design()
    return model.get_design_by_id(id), 200


def add_new_design():
    model = Design()
    data = request.get_json()
    return model.add_new_design(data)
