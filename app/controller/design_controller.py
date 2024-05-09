from flask import request, jsonify
from app.model import Design


def get_designs():
    model = Design()
    res_data = jsonify(model.fetch_all_design())
    return res_data, 200


def get_design_by_id(id):
    model = Design()
    res_data = jsonify(model.get_design_by_id(id))
    return res_data, 200


def add_new_design():
    model = Design()
    req_data = request.get_json()
    res_data = jsonify(model.add_new_design(req_data))
    return res_data
