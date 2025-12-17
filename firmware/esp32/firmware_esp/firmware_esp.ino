#include <WiFi.h>
#include <TinyGPSPlus.h>

// ================== CONFIG RÉSEAU ==================
const char* WIFI_SSID     = "Diegoo";
const char* WIFI_PASSWORD = "88888888";

// Adresse du serveur Node.js (PC où tourne server.js)
const char* SERVER_HOST = "10.55.51.161";  // IP actuelle (ipconfig)
const uint16_t SERVER_PORT = 3000;
const char* SERVER_PATH = "/api/position";


// ================== CONFIG GPS ==================
static const int GPS_RX_PIN = 4; // RX de l'ESP32 (vers TX du NEO-6M)
static const int GPS_TX_PIN = 5; // TX de l'ESP32 (vers RX du NEO-6M)
static const uint32_t GPS_BAUD = 9600;

HardwareSerial gpsSerial(1);
TinyGPSPlus gps;

// ================== CONFIG COORD PAR DEFAUT ==================
const double DEFAULT_LAT = 50.85000200227987;
const double DEFAULT_LNG = 4.453695312563009;


// mémoire de la dernière position GPS valide
double lastGpsLat = DEFAULT_LAT;
double lastGpsLng = DEFAULT_LNG;
unsigned long lastGpsFixMs = 0;

// On considère qu'une donnée GPS est "récente" si < 10s
const unsigned long GPS_VALID_DURATION_MS = 10000;

// ================== CONFIG ENVOI ==================
unsigned long lastSend = 0;
const unsigned long SEND_INTERVAL_MS = 1000; // 1s

// ================== FONCTIONS ==================

void connectWiFi() {
  Serial.print("Connexion au Wi-Fi ");
  Serial.print(WIFI_SSID);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  unsigned long startAttemptTime = millis();
  while (WiFi.status() != WL_CONNECTED && millis() - startAttemptTime < 20000) {
    Serial.print(".");
    delay(500);
  }

  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\nWi-Fi connecté !");
    Serial.print("Adresse IP: ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println("\nÉchec de connexion Wi-Fi.");
  }
}

String boolToJson(bool b) {
  return b ? "true" : "false";
}

void sendStatusToServer(double lat, double lng, bool gpsValid, bool usedDefault) {
  bool wifiConnected = (WiFi.status() == WL_CONNECTED);

  if (!wifiConnected) {
    Serial.println("Wi-Fi déconnecté, tentative de reconnexion...");
    connectWiFi();
    wifiConnected = (WiFi.status() == WL_CONNECTED);
    if (!wifiConnected) {
      Serial.println("Impossible d'envoyer la position, Wi-Fi non disponible");
      return;
    }
  }

  WiFiClient client;
  Serial.print("Connexion au serveur ");
  Serial.print(SERVER_HOST);
  Serial.print(":");
  Serial.println(SERVER_PORT);

  if (!client.connect(SERVER_HOST, SERVER_PORT)) {
    Serial.println("Connexion au serveur échouée.");
    return;
  }

  // Infos réseau
  String wifiSsid = wifiConnected ? WiFi.SSID() : "";
  String wifiIp   = wifiConnected ? WiFi.localIP().toString() : "";
  int wifiRssi    = wifiConnected ? WiFi.RSSI() : 0;

  unsigned long nowMs = millis();

  String body = "{";

  body += "\"lat\":" + String(lat, 8) + ",";
  body += "\"lng\":" + String(lng, 8) + ",";

  // wifi
  body += "\"wifi\":{";
  body += "\"connected\":" + boolToJson(wifiConnected) + ",";
  body += "\"ssid\":\"" + wifiSsid + "\",";
  body += "\"ip\":\"" + wifiIp + "\",";
  body += "\"rssi\":" + String(wifiRssi);
  body += "},";

  // gps
  body += "\"gps\":{";
  body += "\"valid\":" + boolToJson(gpsValid) + ",";
  body += "\"usedDefault\":" + boolToJson(usedDefault) + ",";
  body += "\"lastFixMs\":" + String(lastGpsFixMs);
  body += "},";

  // temps interne ESP (ms depuis boot)
  body += "\"deviceTimeMs\":" + String(nowMs);

  body += "}";

  String request =
    String("POST ") + SERVER_PATH + " HTTP/1.1\r\n" +
    "Host: " + SERVER_HOST + "\r\n" +
    "Content-Type: application/json\r\n" +
    "Connection: close\r\n" +
    "Content-Length: " + body.length() + "\r\n\r\n" +
    body;

  client.print(request);
  Serial.println("Données envoyées au serveur:");
  Serial.println(body);

  // Lecture reponse
  unsigned long timeout = millis();
  while (client.connected() && millis() - timeout < 2000) {
    while (client.available()) {
      String line = client.readStringUntil('\n');
      // Serial.println(line);
      timeout = millis();
    }
  }

  client.stop();
}

void setup() {
  Serial.begin(115200);
  delay(2000);
  Serial.println("Démarrage ESP32 GPS...");

  // UART vers GPS
  gpsSerial.begin(GPS_BAUD, SERIAL_8N1, GPS_RX_PIN, GPS_TX_PIN);

  // Connexion Wi-Fi
  connectWiFi();
}

void loop() {
  // Lecture des données GPS
  while (gpsSerial.available() > 0) {
    char c = gpsSerial.read();
    gps.encode(c);
  }

  // Màj de la dernière position GPS valide
  if (gps.location.isUpdated() && gps.location.isValid()) {
    lastGpsLat = gps.location.lat();
    lastGpsLng = gps.location.lng();
    lastGpsFixMs = millis();

    Serial.print("GPS valide: ");
    Serial.print(lastGpsLat, 8);
    Serial.print(", ");
    Serial.println(lastGpsLng, 8);
  } else {
    // Debug si pas de fix
    static unsigned long lastInfo = 0;
    if (millis() - lastInfo > 2000) {
      lastInfo = millis();
      Serial.println("En attente de fix GPS...");
    }
  }

  // Envoi vers serveur (même sans nouvelle donnée GPS)
  unsigned long now = millis();
  if (now - lastSend >= SEND_INTERVAL_MS) {
    lastSend = now;

    bool gpsRecentlyValid = (lastGpsFixMs > 0) && ((now - lastGpsFixMs) < GPS_VALID_DURATION_MS);

    double sendLat;
    double sendLng;
    bool usedDefault = false;

    if (gpsRecentlyValid) {
      sendLat = lastGpsLat;
      sendLng = lastGpsLng;
      usedDefault = false;
    } else {
      // Pas de valeur GPS récente → envoie la pos par défaut
      sendLat = DEFAULT_LAT;
      sendLng = DEFAULT_LNG;
      usedDefault = true;
    }

    sendStatusToServer(sendLat, sendLng, gpsRecentlyValid, usedDefault);
  }
}
