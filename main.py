from flask import Flask, jsonify
import datetime


app = Flask(__name__)

@app.route("/")
def greetings():
    return "Shalom ✋🏽"

@app.route("/healthcheck")
def healthcheck():
    date = datetime.now().date()
    return jsonify({"message":f"{date}"}), 200