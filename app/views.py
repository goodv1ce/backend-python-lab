from flask import jsonify
from app import app


@app.route("/healthcheck")
def healthcheck():
    return jsonify({"status": "OK"})
