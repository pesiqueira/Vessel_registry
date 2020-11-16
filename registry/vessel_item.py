from flask import Blueprint, request
from dao.vessel import Dao
import json

vessel_item_bp = Blueprint("vessel_item_registry",__name__)
dao = Dao()

@vessel_item_bp.route("/vessel/<code>/items", methods=["GET"])
@vessel_item_bp.route("/vessel/<code>/items/<code_item>", methods=["GET"])
def get_vessel_item(code="",code_item=""):
    try:
        return json.dumps(dao.get_vessel_item(code,code_item))
    except NameError:
        return "Invalid code"

@vessel_item_bp.route("/vessel/<code>/items", methods=["POST"])
def post_vessel_item(code=""):
    try:
        return dao.insert_vessel_item(code,request.get_json())
    except NameError:
        return "Invalid Item Information"

@vessel_item_bp.route("/vessel/<code>/items/deactivate", methods=["POST"])
def deactivate_vessel_item(code):
    try:
        code_items = request.get_json()
        for code_item in code_items:
            dao.deactivate_vessel_item(code,code_item['code'])
        return 'deactivated'
            
    except NameError:
        return "Invalid code"