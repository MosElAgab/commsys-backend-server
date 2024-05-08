from flask import Blueprint
from app.controller import (get_designs, get_design_by_id, add_new_design)

design_bp = Blueprint('design_bp', __name__)

design_bp.route('/', methods=['GET'])(get_designs)
design_bp.route('/', methods=['POST'])(add_new_design)
design_bp.route('/<int:id>', methods=['GET'])(get_design_by_id)