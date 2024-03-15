from flask import request, jsonify
from config import app, db

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Hello Flask"})