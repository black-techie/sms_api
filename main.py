from flask import Flask, request, jsonify
import uuid
import os
from pysondb import db


app = Flask(__name__)


@app.route("/android", methods=["GET", "POST"])
def android():
    a = db.getDb("./json.json")
    sms = a.getAll()
    if request.method == "GET":
        return {"medic-gateway": True}, 200

    if request.method == "POST":
        a.deleteAll()
        if len(sms):
            return jsonify({"messages": sms}), 200


@app.route("/sms", methods=["GET", "POST"])
def sms():
    plate = request.args.get("plate")
    a = db.getDb("./json.json")
    if request.method == "GET":
        a.add(
            {
                "id": str(uuid.uuid4()),
                "to": "0674274382",
                "content": f"""\
                            Urgent: Mobile Phone Usage Detected\n
                                    This is to inform you that a car 
                                    driver was detected using a 
                                    mobile phone while driving.\n
                                    Number plate: {plate}""",
            }
        )

    # if request.method == "POST":
    #     a.add({
    # 		"id": str(uuid.uuid4()),
    # 		"to": "0789105606",
    # 		"content": "testing"
    #     })

    return {"response": "success"}, 200


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT"), host="0.0.0.0")
