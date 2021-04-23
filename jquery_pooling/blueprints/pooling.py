from datetime import datetime

from celery.result import AsyncResult
from flask import request, jsonify
from flask.blueprints import Blueprint
from logging import getLogger

bp = Blueprint("pooling_bp", "pooling_bp")


@bp.route("/pooling", methods=["GET", "POST"])
def pooling_view(*args, **kwargs):
    task_id = request.json["task_id"]
    result = AsyncResult(task_id)
    if not result:
        return "Not found", 404

    status = {
        "task_id": result.task_id,
        "status": result.status,
        "result": result.result
    }

    return jsonify(status), 202
