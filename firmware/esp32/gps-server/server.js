const express = require("express");
const http = require("http");
const { Server } = require("socket.io");
const path = require("path");

const app = express();
const server = http.createServer(app);
const io = new Server(server);

const PORT = 3000;

// Middleware pour parser le JSON entrant
app.use(express.json());

// Servir les fichiers statiques (frontend)
app.use(express.static(path.join(__dirname, "public")));

// Dernière position reçue
let lastPosition = null;

// API appelée par l'ESP32
app.post("/api/position", (req, res) => {
  const { lat, lng, wifi, gps, deviceTimeMs } = req.body;

  if (typeof lat !== "number" || typeof lng !== "number") {
    return res.status(400).json({ error: "lat et lng doivent être des nombres" });
  }

  const now = Date.now();

  lastPosition = {
    lat,
    lng,
    wifi: wifi || null,
    gps: gps || null,
    deviceTimeMs: deviceTimeMs || null,
    timestamp: now   // heure de réception côté serveur (ms depuis 1970)
  };

  console.log("Nouvelle position reçue:", lastPosition);

  // Envoi à tous les clients Web connectés
  io.emit("position", lastPosition);

  res.json({ status: "ok" });
});

// Optionnel : endpoint pour voir la dernière data dans un navigateur / Postman
app.get("/api/status", (req, res) => {
  if (!lastPosition) {
    return res.json({ hasData: false });
  }
  res.json({ hasData: true, lastPosition });
});

// Socket.IO : quand un client Web se connecte
io.on("connection", (socket) => {
  console.log("Client Web connecté:", socket.id);

  // On lui envoie directement la dernière position connue s'il y en a une
  if (lastPosition) {
    socket.emit("position", lastPosition);
  }

  socket.on("disconnect", () => {
    console.log("Client Web déconnecté:", socket.id);
  });
});

server.listen(PORT, () => {
  console.log(`Serveur démarré sur http://localhost:${PORT}`);
});
