from flask import Flask, request, jsonify
import uuid
import os


app = Flask(__name__)

sms = []

@app.route("/android", methods=["GET", "POST"])
def android():
    global sms
    if request.method == "GET":
        return {"medic-gateway": True}, 200
    
    if request.method == "POST":
        if len(sms):
            sms_cpy = sms
            sms =[]
            return jsonify({"messages": sms_cpy}), 200

@app.route("/sms", methods = ["GET", "POST"])
def sms():
    global sms
    if request.method == "GET":
        sms.append({
			"id": str(uuid.uuid4()),
			"to": "0789105606",
			"content": "testing"
        })

    if request.method == "POST":
        sms.append({
			"id": str(uuid.uuid4()),
			"to": "0789105606",
			"content": "testing"
        })


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv('PORT'), host="0.0.0.0")
