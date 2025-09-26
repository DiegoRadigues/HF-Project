# Vision & critères d’acceptation (Definition of Done)

## Vision
Le projet vise à concevoir une **solution RF sur PCB** intégrant :
- Une **carte embarquée** avec ESP32 (Wi-Fi/BLE), GPS AM-M8Q-0, LoRa RFM95 (868 MHz) et gestion batterie 2S via BQ25798.
- Une **carte antenne PCB dédiée** pour la bande 868 MHz, simulée, implémentée et caractérisée.
- Un **firmware de démonstration** permettant de valider la communication LoRa, la réception GPS et la connectivité Wi-Fi/BLE.
- Une **documentation style carte de développement** (datasheet, schémas, quickstart, tutoriels).
- Un **journal de bord partagé** servant de base pour le rapport et la présentation finale.

L’objectif est de fournir un **POC fonctionnel industriel**, validé à la fois par la conception, la simulation et les tests instrumentés (VNA, spectre, oscilloscope).

---

## Definition of Done (DoD)

| Domaine | Critères d’acceptation |
|---------|------------------------|
| **Fonctionnel RF** | - Communication LoRa point-à-point ≥ 300 m en champ libre<br>- Antenne accordée : S11 < –10 dB @ 868 MHz<br>- Rendement antenne ≥ 50 % |
| **GPS** | - Acquisition du fix < 60 s en conditions dégagées (TTFF)<br>- Précision < 5 m en mode autonome |
| **Wi-Fi/BLE** | - Scan AP et connexion réussie à un réseau Wi-Fi<br>- Détection BLE périphériques à proximité |
| **Consommation** | - Courant repos (ESP32 deep sleep) < 20 µA (hors GPS/LoRa)<br>- Autonomie minimale > 24h en cycle périodique (1 trame LoRa/min) |
| **EMI/CEM** | - Pas de pics > –30 dBm en pré-scan (référence EN 300 220)<br>- Simulations EMI/CEM disponibles et comparées aux mesures |
| **Documentation** | - Datasheet style dev board (schémas, pinout, specs électriques)<br>- Quickstart (flash firmware, tests LoRa/GPS/Wi-Fi)<br>- Tutoriels simulation antenne & mesures VNA |
| **POC validé** | - PCB fabriqué et assemblé<br>- Antenne caractérisée en VNA et testée en portée<br>- Firmware de démo intégré et fonctionnel<br>- Rapport/log complet et oral réussi |

---
