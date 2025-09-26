# Documentation style « Dev Board » — Checklist

## À inclure absolument

- [ ] **Introduction**
  - Objectif du board (POC RF/IoT)
  - Modules intégrés (ESP32, GPS, LoRa, PMIC)

- [ ] **Caractéristiques principales**
  - Fréquences supportées (LoRa 868 MHz, Wi-Fi/BLE, GPS)
  - Antenne (type, bande, rendement visé)
  - Dimensions PCB

- [ ] **Spécifications électriques**
  - Tension entrée USB-C
  - Batterie supportée (2S Li-Ion)
  - Consommations (actif, sleep, deep sleep)

- [ ] **Schéma fonctionnel** (block diagram simplifié)

- [ ] **Pinout & interfaces**
  - Broches ESP32 accessibles
  - Connecteurs (SMA, USB-C, UART debug, I²C, SPI)

- [ ] **Guide de démarrage rapide**
  - Alimentation (USB-C, batterie)
  - Programmation (ESP-IDF/Arduino)
  - Premier test (logs UART, Wi-Fi scan)
  - GPS test (NMEA visible)
  - LoRa test (ping/pong)

- [ ] **Tutoriels pratiques**
  - Simulation antenne (OpenEMS)
  - Mesure VNA (S11, BW)
  - Range test LoRa
  - GPS TTFF
  - EMI/CEM pré-scan

- [ ] **Exigences IA**
  - Citer usage IA dans `AI_SOURCES.md` ou en note

- [ ] **Organisation des fichiers docs**
  - `/docs/datasheet/Board_Datasheet.pdf`
  - `/docs/quickstart/Quickstart.md`
  - `/docs/tutorials/`
  - `/docs/images/`
  - `/docs/logs/`