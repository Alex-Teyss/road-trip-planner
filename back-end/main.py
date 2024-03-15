from flask import request, jsonify
from config import app, db

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Hello Flask"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)