# Plan de validation HW/SW

Le plan de validation couvre à la fois la partie **hardware** (mesures RF, alimentation, EMI/CEM) et la partie **software** (protocoles LoRa, GPS, Wi-Fi/BLE).  
Chaque test est lié à un script ou une procédure documentée dans `/tests/`.

---

## 1. Scripts & outils de test

- **RF** :
  - Python + SCPI (PyVISA) pour piloter VNA/spectre → export `.csv`.
  - Scripts Matplotlib pour tracer S11 et BW.
- **LoRa** :
  - Firmware ping/pong (ESP32 ↔ RFM95).
  - Log UART RSSI/SNR.
- **GPS** :
  - Parser NMEA → log TTFF et position.
  - Script Python pour extraire GGA, RMC.
- **Wi-Fi/BLE** :
  - Scan SSID/AP.
  - Log RSSI, latence de connexion.
- **Conso** :
  - Mesure ampèremètre en modes : actif, sleep, deep sleep.
- **EMI/CEM** :
  - OpenEMS simulations.
  - Pre-scan labo (spectre, LISN).

---

## 2. Matrice de validation

| Module | Test | Méthode | Critère réussite | Artefacts |
|--------|------|---------|------------------|-----------|
| **LoRa** | Ping/pong range test | 300 m champ libre | PER < 5 % | `lora_range.log` |
| **LoRa** | RSSI vs distance | Log UART | RSSI cohérent (–120 dBm sensibilité max) | `rssi_curve.csv` |
| **GPS** | TTFF | Test terrain | Fix < 60 s | `gps_ttff.log` |
| **GPS** | Précision | Moyenne position | < 5 m | `gps_accuracy.md` |
| **Wi-Fi** | Scan AP | Firmware ESP32 | AP visible, RSSI loggé | `wifi_scan.log` |
| **BLE** | Scan périphériques | Firmware ESP32 | Détection périph. | `ble_scan.log` |
| **PMIC** | Charge/décharge | Multimètre + USB-C | Vbat stable, charge OK | `pmic_test.md` |
| **Conso** | Deep sleep | Ampèremètre | < 20 µA | `power_sleep.csv` |
| **RF** | S11 antenne | VNA | < –10 dB @ 868 MHz | `s11_meas.csv` |
| **RF** | Bande passante | VNA | ≥ 2 MHz | `bw_meas.png` |
| **EMI** | Pre-scan | Spectrum | Aucun pic > –30 dBm | `emi_report.pdf` |

---

## 3. Validation incrémentale par phases

- **Phase 2** : Vérifier UART log, Wi-Fi scan, GPS NMEA.  
- **Phase 3** : Simulations antenne → S11 (OpenEMS).  
- **Phase 4** : Protocoles de test rédigés, EMI/CEM simulation.  
- **Phase 5** : Mesures réelles (VNA, spectre, LoRa portée, GPS TTFF).  
- **Phase 6** : Validation intégrée (POC complet + démo).

---

## 4. Gabarits de rapport

Chaque test doit produire :
- **Titre & description** (objectif du test).  
- **Méthode** (procédure + setup).  
- **Résultats** (fichiers CSV/plots/logs).  
- **Analyse** (succès/échec, points à améliorer).  
- **Décision** (validé ou non).  

Tous les rapports seront stockés dans `/tests/` et référencés dans le rapport final.