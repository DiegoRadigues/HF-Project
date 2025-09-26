# Work Breakdown Structure (WBS) & RACI

La WBS est organisée par phases (alignées sur le projet).  
Chaque **Epic** se décompose en **User Stories**, elles-mêmes déclinées en **tâches atomiques** estimées ≤ 1 jour.  
Chaque tâche est accompagnée d’un **exemple d’Issue GitHub** réutilisable.

---

## Phase 1 — Implémentation PCB (+ fabrication)

### Epic : Concevoir et fabriquer la carte embarquée et la carte antenne

#### User Stories
- [S1] Réaliser le schéma électrique complet (ESP32, GPS, LoRa, PMIC).
- [S2] Effectuer le placement & routage sous contraintes JLCPCB.
- [S3] Générer les fichiers de fabrication (Gerbers, BOM, Pick&Place).

#### Tâches atomiques

| ID | Tâche | Est. (h) | Dépendances | Artefacts | R | A | C | I |
|----|-------|----------|--------------|-----------|---|---|---|---|
| P1-S1.1 | Schéma ESP32-C3 + périphériques | 6 | BOM validée | `.sch` | A | B | C | - |
| P1-S1.2 | Schéma GPS/LoRa/PMIC | 6 | P1-S1.1 | `.sch` | B | A | C | - |
| P1-S2.1 | Placement PCB embarqué | 4 | P1-S1.2 | `.kicad_pcb` | C | A | B | - |
| P1-S2.2 | Routage RF 50 Ω + lignes diff USB | 6 | P1-S2.1 | `.kicad_pcb` | A | B | C | - |
| P1-S2.3 | Placement antenne PCB séparée | 3 | S2.1 | `.kicad_pcb` | B | A | C | - |
| P1-S3.1 | DRC/ERC et corrections | 3 | Routage fini | Report DRC/ERC | B | A | C | - |
| P1-S3.2 | Export Gerbers/BOM/PnP | 2 | P1-S3.1 | Gerbers | C | A | B | - |

---

## Phase 2 — Software & Lab concept

### Epic : Préparer firmware minimal et définir stratégie antenne

#### User Stories
- [S1] Firmware stub ESP32 : UART log + scan Wi-Fi/BLE.
- [S2] Intégrer driver GPS (lecture NMEA).
- [S3] Étudier options antennes 868 MHz et valider choix.

#### Tâches atomiques

| ID | Tâche | Est. (h) | Dépendances | Artefacts | R | A | C | I |
|----|-------|----------|--------------|-----------|---|---|---|---|
| P2-S1.1 | Init projet ESP-IDF + UART log | 3 | PCB pinout | main.c | A | B | C | - |
| P2-S1.2 | Test Wi-Fi scan + log RSSI | 3 | S1.1 | UART log | B | A | C | - |
| P2-S2.1 | Parser NMEA du GPS | 4 | UART dispo | gps.c | C | A | B | - |
| P2-S3.1 | Recherche types antennes PCB 868 MHz | 2 | - | Rapport | A | B | C | - |
| P2-S3.2 | Choix antenne validé (IFAA/monopole/etc.) | 2 | S3.1 | Decision log | B | A | C | - |

---

## Phase 3 — Simulation & implémentation antenne (+ fabrication)

### Epic : Concevoir, simuler et fabriquer une antenne PCB accordée à 868 MHz

#### User Stories
- [S1] Modéliser antenne candidate sous OpenEMS.
- [S2] Optimiser matching (S11).
- [S3] Exporter design pour fabrication.

#### Tâches atomiques

| ID | Tâche | Est. (h) | Dépendances | Artefacts | R | A | C | I |
|----|-------|----------|--------------|-----------|---|---|---|---|
| P3-S1.1 | Modèle OpenEMS antenne IFA | 4 | P2-S3.2 | `.xml` | A | B | C | - |
| P3-S1.2 | Sweep paramètres (longueur/width) | 4 | S1.1 | S11 plots | B | A | C | - |
| P3-S2.1 | Matching network π-LC (Qucs) | 4 | S1.2 | `.sch`, BOM | C | A | B | - |
| P3-S3.1 | Export Gerbers antenne PCB | 2 | S2.1 | Gerbers | B | A | C | - |

---

## Phase 4 — Protocoles & tests (HW/SW), pré-caractérisation EMI/CEM

### Epic : Définir et exécuter protocoles de test initiaux

#### User Stories
- [S1] Définir plan de test VNA, S11, bande passante.
- [S2] Préparer scripts EMI/CEM (OpenEMS).
- [S3] Déployer firmware pré-test (LoRa ping).

#### Tâches atomiques

| ID | Tâche | Est. (h) | Dépendances | Artefacts | R | A | C | I |
|----|-------|----------|--------------|-----------|---|---|---|---|
| P4-S1.1 | Rédiger plan de test RF | 2 | Phase 3 | Plan doc | A | B | C | - |
| P4-S2.1 | Simulation EMI avec OpenEMS | 4 | PCB Gerbers | Report | C | A | B | - |
| P4-S3.1 | Firmware LoRa ping/pong | 4 | ESP32 SPI LoRa | lora.c | B | A | C | - |

---

## Phase 5 — Tests instrumentés (VNA, spectre, oscillo)

### Epic : Valider performances antenne et firmware intégré

#### User Stories
- [S1] Mesurer S11, BW et rendement antenne.
- [S2] Tester portée LoRa.
- [S3] Valider GPS fix et Wi-Fi.

#### Tâches atomiques

| ID | Tâche | Est. (h) | Dépendances | Artefacts | R | A | C | I |
|----|-------|----------|--------------|-----------|---|---|---|---|
| P5-S1.1 | Calibration VNA (SOLT) | 2 | Matériel dispo | Cal report | A | B | C | - |
| P5-S1.2 | Mesure S11 antenne | 2 | S1.1 | CSV, plot | B | A | C | - |
| P5-S2.1 | Test LoRa portée 300 m | 4 | LoRa firmware | Log RSSI | C | A | B | - |
| P5-S3.1 | GPS TTFF test terrain | 3 | Firmware GPS | Logs NMEA | A | B | C | - |
| P5-S3.2 | Wi-Fi/BLE scan | 2 | P2-S1.2 | Log | B | A | C | - |

---

## Phase 6 — Examen oral & rapport

### Epic : Présenter et documenter le POC

#### User Stories
- [S1] Rédiger rapport basé sur journal/log.
- [S2] Préparer présentation orale.
- [S3] Démo du POC fonctionnel.

#### Tâches atomiques

| ID | Tâche | Est. (h) | Dépendances | Artefacts | R | A | C | I |
|----|-------|----------|--------------|-----------|---|---|---|---|
| P6-S1.1 | Compiler logs + images | 3 | Toutes phases | Rapport.md | A | B | C | - |
| P6-S2.1 | Préparer slides 30 min | 4 | Rapport draft | Slides | B | A | C | - |
| P6-S3.1 | Répétition démo | 2 | Hardware validé | Notes | C | A | B | - |

---