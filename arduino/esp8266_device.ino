/*
===========================================================
 ESP8266 IoT DEVICE TEMPLATE (DAY 11 PROJECT)
===========================================================

THIS FILE IS FOR REAL HARDWARE DEPLOYMENT (NOT SIMULATION)

-----------------------------------------------------------
 HOW THIS FITS INTO YOUR SYSTEM
-----------------------------------------------------------

 DEVICE (ESP8266 / Arduino)
        ↓ HTTP POST (WiFi)
 Flask API (python/api.py)
        ↓
 SQLite Database (database/iot.db)
        ↓
 Dashboard (dashboard/index.html)

-----------------------------------------------------------
 WHAT TO CHANGE WHEN MOVING TO REAL HARDWARE
-----------------------------------------------------------

 1. Replace WiFi credentials below
 2. Replace server IP (your PC or cloud server)
 3. Ensure Flask API is running on same network
 4. Update endpoint if changed (/event)
 5. Match payload structure with API

-----------------------------------------------------------
 SIMULATION vs REAL MODE
-----------------------------------------------------------

 CURRENT PROJECT:
 - edge_simulator.py generates fake sensor data

 REAL HARDWARE:
 - THIS Arduino/ESP8266 code replaces simulator

 ONLY ONE SHOULD RUN AT A TIME:
 - simulator (testing)
 - OR hardware device (production)

===========================================================
*/

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

// -------------------------
// WIFI CONFIG
// -------------------------
const char* ssid = "YOUR_WIFI_NAME";
const char* password = "YOUR_WIFI_PASSWORD";

// -------------------------
// API ENDPOINT
// -------------------------
// Change IP to your Flask server machine
const char* serverUrl = "http://192.168.1.10:5000/event";

// -------------------------
// DEVICE INFO
// -------------------------
String device_id = "TEMP_01";
String device_type = "temp_sensor";

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi Connected");
}

void loop() {

  if (WiFi.status() == WL_CONNECTED) {

    WiFiClient client;
    HTTPClient http;

    http.begin(client, serverUrl);
    http.addHeader("Content-Type", "application/json");

    // -------------------------
    // SIMULATED SENSOR VALUE (replace with real sensor later)
    // -------------------------
    float temperature = random(200, 400) / 10.0;

    // -------------------------
    // ONLY SEND IF ABOVE THRESHOLD (EDGE LOGIC)
    // -------------------------
    if (temperature > 30.0) {

      String payload = "{";
      payload += "\"device_id\":\"" + device_id + "\",";
      payload += "\"device_type\":\"" + device_type + "\",";
      payload += "\"event_type\":\"threshold_alert\",";
      payload += "\"payload\":{\"temperature\":" + String(temperature) + "}";
      payload += "}";

      int httpResponseCode = http.POST(payload);

      Serial.print("Sent data: ");
      Serial.println(payload);
      Serial.print("Response: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  }

  delay(5000); // send every 5 seconds
}