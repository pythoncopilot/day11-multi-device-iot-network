# 🌐 Edge IoT Multi-Device System (Day 11)

This project is a **real-world IoT architecture simulation** built with edge computing concepts, REST APIs, and hardware-ready firmware.

It includes:
- ESP8266 / Arduino hardware template (production-ready)
- Python Flask REST API
- SQLite event-based database
- Edge computing simulator
- Web dashboard (HTML + JavaScript)
- GitHub CI pipeline

---

# 🚀 System Architecture

ESP8266 / Edge Simulator  
→ Flask API (Ingestion Layer)  
→ SQLite Database (Event Storage)  
→ State API (/state)  
→ Dashboard (Live Visualization)

---

# 🧠 Core Concepts Implemented

## ✔ Edge Computing
Devices only send meaningful events:
- threshold alerts
- motion triggers
- state changes

## ✔ Event-Based IoT Design
Instead of continuous streaming, system sends:
- important events only
- filtered sensor data

## ✔ Multi-Device Support
Simulated devices:
- TEMP_01 (temperature sensor)
- MOTION_01 (motion sensor)
- TANK_01 (water level sensor)

## ✔ Environment Switching
Supports deployment modes:
- LOCAL → 127.0.0.1
- REMOTE → Raspberry Pi / LAN IP

---

# 📁 Project Structure

day11-edge-iot/
├── python/
│   ├── api.py              # Flask REST API
│   ├── db.py               # SQLite database layer
│   ├── edge_simulator.py   # Edge-based IoT simulator
│
├── dashboard/
│   └── index.html          # Live IoT dashboard
│
├── arduino/
│   └── esp8266_device.ino  # Hardware firmware (ESP8266)
│
├── database/
│   └── iot.db              # SQLite database
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
└── README.md

---

# ⚙️ Configuration (IMPORTANT)

Each component supports LOCAL / REMOTE switching.

## Python API
MODE = "LOCAL"

## Edge Simulator
MODE = "LOCAL"

## Dashboard (JavaScript)
MODE = "LOCAL"

## ESP8266 Firmware
Set server IP manually:
http://192.168.1.10:5000/event

---

# 🚀 How to Run (Local Setup)

## 1. Start Flask API
python python/api.py

## 2. Run Edge Simulator
python python/edge_simulator.py

## 3. Open Dashboard
Open:
dashboard/index.html

---

# 📡 API Endpoints

## POST /event
Used by devices to send events

Example:
{
  "device_id": "TEMP_01",
  "device_type": "temp_sensor",
  "event_type": "threshold_alert",
  "payload": {
    "temperature": 32.5
  }
}

---

## GET /state
Returns latest state of all devices

---

# 🔥 Hardware Ready (ESP8266)

File:
arduino/esp8266_device.ino

Features:
- WiFi connection
- HTTP POST to Flask API
- Edge threshold logic
- Ready for real sensors

---

# 🧠 Learning Outcomes

- REST API design for IoT systems
- Edge computing logic implementation
- Event-driven architecture
- Multi-device simulation
- Frontend IoT dashboard
- Hardware + software integration

---

# 🚀 Future Improvements

- MQTT integration (industrial IoT standard)
- WebSocket real-time dashboard
- Cloud deployment (AWS / Render)
- Device authentication system
- Time-series analytics charts

---

# 👨‍💻 Author

30-day Embedded + IoT Learning Journey