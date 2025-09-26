# Plan de tests par itération

Les tests sont organisés par phase/itération, avec description, méthode de mesure et critères de réussite.  
Chaque résultat sera loggé dans `/tests/` (CSV + rapports Markdown + captures d’écran).

---

## Tableau des tests

| Phase | Test | Méthode / Outils | Critère de réussite | Artefacts |
|-------|------|------------------|----------------------|-----------|
| **P2** | Wi-Fi/BLE scan | Firmware ESP32 + log UART | AP visible + RSSI affiché | `wifi_scan.log` |
| **P2** | GPS lecture NMEA | UART parse → NMEA | Trame GGA valide reçue | `gps_nmea.log` |
| **P3** | Antenne S11 (simulation) | OpenEMS sweep | f₀ ≈ 868 MHz, S11 < –10 dB | `antenna_s11_sim.png` |
| **P3** | Matching LC (Qucs) | Network simulation | |S11| amélioré au point d’accord | `matching.sch` |
| **P4** | Plan de test VNA | Rédaction protocole | Procédure claire validée | `plan_test_rf.md` |
| **P4** | EMI/CEM pré-scan | OpenEMS + Spectrum (pre-scan) | Pas de dépassement > –30 dBm | `emi_pre_scan.pdf` |
| **P5** | S11 antenne (mesure réelle) | VNA calibration SOLT | S11 < –10 dB @ 868 MHz | `s11_meas.csv` |
| **P5** | Bande passante | VNA BW 10 dB | BW ≥ 2 MHz (LoRa) | `bw_report.png` |
| **P5** | Rendement antenne | Champ proche → champ lointain | η ≥ 50 % | `efficiency_report.md` |
| **P5** | Portée LoRa | Test terrain 300 m | PER < 5 % @ 300 m | `lora_range.log` |
| **P5** | GPS TTFF | Extérieur dégagé | Fix < 60 s | `gps_ttff.log` |
| **P5** | Wi-Fi/BLE validation | Scan + connexion | Connexion stable à AP | `wifi_test.log` |
| **P5** | Consommation | Ampèremètre, mode deep sleep | < 20 µA (ESP32 seul) | `power_meas.csv` |

---

## Protocoles associés
- **Calibration VNA** : méthode SOLT, référence au plan de test.  
- **Logs** : format CSV/Markdown horodaté.  
- **Scripts** : Python SCPI pour récupérer S11, Matplotlib pour plots.  
- **EMI/CEM** : modélisation dans OpenEMS + pre-scan avec LISN.  
- **LoRa test** : ping/pong, log RSSI/SNR en UART.  
- **GPS test** : parse NMEA, calcul TTFF.  

---

## Validation incrémentale
- Chaque phase doit livrer **au moins 1 test réussi** validant un module (Wi-Fi, GPS, RF, antenne).  
- La validation finale repose sur la matrice complète (tous critères atteints).
