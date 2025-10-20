from HealthCheck import app, jsonify
import datetime

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    date = datetime.datetime.now()
    return jsonify({"message":f"{date}"}), 200