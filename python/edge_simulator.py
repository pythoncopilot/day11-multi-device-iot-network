"""
========================================================
 EDGE SIMULATOR (LOCAL / REMOTE READY)
========================================================
"""

import requests
import random
import time

# --------------------------
# CONFIG
# --------------------------
MODE = "LOCAL"

if MODE == "LOCAL":
    BASE_URL = "http://127.0.0.1:5000"
else:
    BASE_URL = "http://192.168.1.10:5000"  # CHANGE THIS

API = BASE_URL + "/event"


def send(data):
    try:
        requests.post(API, json=data)
        print("sent:", data)
    except Exception as e:
        print("error:", e)


while True:

    temp = round(random.uniform(20, 40), 2)
    if temp > 30:
        send({
            "device_id": "TEMP_01",
            "device_type": "temp_sensor",
            "event_type": "threshold_alert",
            "payload": {"temperature": temp}
        })

    motion = random.choice([True, False])
    if motion:
        send({
            "device_id": "MOTION_01",
            "device_type": "motion_sensor",
            "event_type": "trigger",
            "payload": {"motion": True}
        })

    level = random.randint(0, 100)
    if level < 30:
        send({
            "device_id": "TANK_01",
            "device_type": "tank_sensor",
            "event_type": "low_level",
            "payload": {"water_level": level}
        })

    time.sleep(2)