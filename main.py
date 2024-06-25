from flask import Flask, request, jsonify
import uuid
import os
from pysondb import db


app = Flask(__name__)


@app.route("/android", methods=["GET", "POST"])
def android():
    a=db.getDb("./json.json")
    sms = a.getAll()
    if request.method == "GET":
        return {"medic-gateway": True}, 200
    
    if request.method == "POST":
        a.deleteAll()
        if len(sms):
            return jsonify({"messages": sms}), 200

@app.route("/sms", methods = ["GET", "POST"])
def sms():
    a=db.getDb("./json.json")
    if request.method == "GET":
        a.add({
			"id": str(uuid.uuid4()),
			"to": "0789105606",
			"content": "testing"
        })

    if request.method == "POST":
        a.add({
			"id": str(uuid.uuid4()),
			"to": "0789105606",
			"content": "testing"
        })


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv('PORT'), host="0.0.0.0")
