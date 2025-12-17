// Initialisation de la carte
const DEFAULT_LAT = 50.84945987146152;
const DEFAULT_LNG = 4.4530963329308415;

let map = L.map("map").setView([DEFAULT_LAT, DEFAULT_LNG], 15);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution: "&copy; OpenStreetMap contributors"
}).addTo(map);

let marker = L.marker([DEFAULT_LAT, DEFAULT_LNG]).addTo(map);
marker.bindPopup("En attente de données GPS...").openPopup();

// DOM elements
const srvStatusSpan = document.getElementById("srv-status");
const devStatusSpan = document.getElementById("dev-status");
const coordsSpan = document.getElementById("coords");
const lastTimeSpan = document.getElementById("last-time");

const wifiSsidSpan = document.getElementById("wifi-ssid");
const wifiIpSpan = document.getElementById("wifi-ip");
const wifiRssiSpan = document.getElementById("wifi-rssi");
const wifiConnectedSpan = document.getElementById("wifi-connected");

const gpsValidSpan = document.getElementById("gps-valid");
const gpsDefaultSpan = document.getElementById("gps-default");
const gpsLastFixSpan = document.getElementById("gps-lastfix");
const devTimeSpan = document.getElementById("dev-time");

// Connexion Socket.IO
const socket = io();

// Pour savoir si on a déjà reçu une data
let hasData = false;

socket.on("connect", () => {
  srvStatusSpan.textContent = "Serveur : connecté";
});

socket.on("disconnect", () => {
  srvStatusSpan.textContent = "Serveur : déconnecté";
  devStatusSpan.textContent = "Appareil : inconnu";
});

// Quand on reçoit une position
socket.on("position", (data) => {
  hasData = true;

  const {
    lat,
    lng,
    wifi,
    gps,
    timestamp,
    deviceTimeMs
  } = data;

  if (typeof lat !== "number" || typeof lng !== "number") return;

  const latLng = [lat, lng];

  marker.setLatLng(latLng);
  marker.setPopupContent(
    `Position reçue<br>Lat: ${lat.toFixed(6)}<br>Lng: ${lng.toFixed(6)}`
  );

  map.setView(latLng, map.getZoom());

  coordsSpan.textContent = `Lat: ${lat.toFixed(6)}, Lng: ${lng.toFixed(6)}`;

  // Heure de la dernière position (heure serveur)
  if (timestamp) {
    const d = new Date(timestamp);
    lastTimeSpan.textContent =
      "Dernière position : " + d.toLocaleString();
  } else {
    lastTimeSpan.textContent = "Dernière position : inconnue";
  }

  // Infos Wi-Fi
  if (wifi) {
    wifiConnectedSpan.textContent = wifi.connected ? "Oui" : "Non";
    wifiSsidSpan.textContent = wifi.ssid || "---";
    wifiIpSpan.textContent = wifi.ip || "---";
    wifiRssiSpan.textContent = wifi.rssi || "---";

    devStatusSpan.textContent = wifi.connected
      ? "Appareil : connecté au Wi-Fi"
      : "Appareil : Wi-Fi déconnecté";
  } else {
    wifiConnectedSpan.textContent = "---";
    wifiSsidSpan.textContent = "---";
    wifiIpSpan.textContent = "---";
    wifiRssiSpan.textContent = "---";
    devStatusSpan.textContent = "Appareil : info réseau inconnue";
  }

  // Infos GPS
  if (gps) {
    gpsValidSpan.textContent = gps.valid ? "Oui" : "Non";
    gpsDefaultSpan.textContent = gps.usedDefault ? "Oui (coord. par défaut)" : "Non (vraie position GPS)";
    gpsLastFixSpan.textContent =
      typeof gps.lastFixMs === "number" ? gps.lastFixMs + " ms" : "---";
  } else {
    gpsValidSpan.textContent = "---";
    gpsDefaultSpan.textContent = "---";
    gpsLastFixSpan.textContent = "---";
  }

  // Temps interne de l'appareil
  if (typeof deviceTimeMs === "number") {
    devTimeSpan.textContent = deviceTimeMs + " ms";
  } else {
    devTimeSpan.textContent = "---";
  }
});
