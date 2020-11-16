from flask import Blueprint, request
from dao.vessel import Dao
vessel_bp = Blueprint("vessel_registry",__name__)
dao = Dao()

@vessel_bp.route("/vessel", methods=["GET"])
@vessel_bp.route("/vessel/<code>", methods=["GET"])
def get_vessel(code=""):
    try:
        return dao.get_vessel(code)
    except NameError:
        return "Invalid code"

@vessel_bp.route("/vessel", methods=["POST"])
def post_vessel():
    try:
        return dao.create_vessel(request.get_json())
    except NameError:
        return "Invalid Vessel Information"

@vessel_bp.route("/vessel/<code>", methods=["DELETE"])
def delete_vessel(code):
    try: 
        return dao.delete_vessel(code)
    except NameError:
        return "Invalid code"