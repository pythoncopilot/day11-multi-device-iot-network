"""
========================================================
 CONFIGURATION MODE: LOCAL vs REMOTE DEPLOYMENT
========================================================

LOCAL:
- API runs on same machine
- ESP + simulator use 127.0.0.1

REMOTE:
- API runs on Raspberry Pi / server
- Devices use LAN IP (e.g., 192.168.1.10)

Change MODE below only
========================================================
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import db

# --------------------------
# CONFIG
# --------------------------
MODE = "LOCAL"

if MODE == "LOCAL":
    HOST = "127.0.0.1"
    PORT = 5000
else:
    HOST = "0.0.0.0"
    PORT = 5000


app = Flask(__name__)
CORS(app)

db.init_db()


@app.route("/")
def home():
    return jsonify({"status": "IoT Edge API Running"})


# --------------------------
# EVENT INGESTION
# --------------------------
@app.route("/event", methods=["POST"])
def ingest_event():
    data = request.json

    db.insert_event(
        data.get("device_id"),
        data.get("device_type"),
        data.get("event_type"),
        data.get("payload")
    )

    return jsonify({"status": "stored"})

# --------------------------
# LATEST STATE
# --------------------------
@app.route("/state", methods=["GET"])
def state():
    rows = db.get_latest_per_device()

    result = []
    for r in rows:
        result.append({
            "id": r[0],
            "device_id": r[1],
            "device_type": r[2],
            "event_type": r[3],
            "payload": r[4],
            "timestamp": r[5]
        })

    return jsonify(result)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)