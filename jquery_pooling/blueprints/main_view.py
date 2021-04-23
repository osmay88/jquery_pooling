from flask import render_template, request, jsonify
from flask.blueprints import Blueprint
from jquery_pooling.task import create_task

bp = Blueprint("main_view_bp", "main_view_bp")


@bp.route("/", methods=["GET", "POST"])
def main_view(*args, **kwargs):
    if request.method == "GET":
        return render_template("index.html", **{})
    else:
        task = create_task.delay(3)
        return jsonify({"task_id": task.id}), 202
