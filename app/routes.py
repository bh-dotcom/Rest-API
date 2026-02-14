from flask import Blueprint, jsonify
from .service import get_transactions

bp = Blueprint("main", __name__)

@bp.route("/transactions/<int:user_id>")
def transactions(user_id):
    data = get_transactions(user_id)
    return jsonify(data)

@bp.route("/health")
def health():
    return {"status": "UP"}, 200
