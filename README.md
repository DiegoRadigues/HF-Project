# HF-Project

Proof of Concept (POC) industriel : conception d’une solution RF sur PCB intégrant ESP32, GPS, LoRa 868 MHz et une antenne dédiée, avec simulation, implémentation et caractérisation.

---

## Objectif
- Démontrer une chaîne hardware + software fonctionnelle :
  - Carte embarquée (ESP32, GPS, LoRa, PMIC, USB-C).
  - Carte antenne PCB 868 MHz conçue, simulée et caractérisée.
  - Firmware de démonstration : LoRa ping/pong, GPS NMEA, Wi-Fi/BLE scan.
- Fournir une documentation style carte de développement (datasheet, quickstart, tutoriels).
- Tenir un journal de bord continu servant de base au rapport final.

---

## Plan de projet
Le projet est découpé en 6 phases, chacune avec livrables.

- [Project Plan complet](project/PROJECT_PLAN.md)
- Sections détaillées :
  1. [Vision & DoD](project/01_Vision_DoD.md)  
  2. [WBS & RACI](project/02_WBS_RACI.md)  
  3. [Planning & jalons](project/03_Planning.md)  
  4. [Plan de tests](project/04_Tests.md)  
  5. [Architecture PCB](project/05_Architecture_PCB.md)  
  6. [Stratégie antenne](project/06_Strategie_Antenne.md)  
  7. [Validation HW/SW](project/07_Validation_HW_SW.md)  
  8. [Docs « dev board »](project/08_Documentation_DevBoard.md)  
  9. [Repo GitHub](project/09_Repo_GitHub.md)  
  10. [Risques & qualité](project/10_Risques_Qualite.md)

---

## Structure du repo

- `/project/` → plan de projet (sections 01–10).  
- `/docs/` → documentation utilisateur (datasheet, quickstart, tutoriels, images).  
- `/hardware/` → schémas KiCad, Gerbers, antenne, EMI/CEM.  
- `/firmware/` → drivers ESP32 + exemples.  
- `/tests/` → plans, scripts et rapports de tests.  
- `/logs/` → journal de bord (suivi continu).  
- `/ci/` → workflows CI/CD.  
- `/.github/` → templates issues/PR.  

---

## Journal de bord
- [Index du journal](logs/journal_index.md)  
- Journaux individuels : `/logs/journal/YYYY-MM-DD.md`

---

## Documentation
- [Datasheet (à compléter)](docs/datasheet/)  
- [Quickstart (flash, premiers tests)](docs/quickstart/)  
- [Tutoriels pratiques](docs/tutorials/)  

---

## Développement

### Hardware
- Schémas et PCB : [`/hardware/kicad/`](hardware/kicad/)  
- Gerbers + BOM : [`/hardware/fabrication/`](hardware/fabrication/)  
- Antenne PCB 868 MHz : [`/hardware/antenna/`](hardware/antenna/)  

### Firmware
- ESP32 + drivers : [`/firmware/esp32/`](firmware/esp32/)  
- Scripts Python : [`/firmware/tools/`](firmware/tools/)  

### Tests
- RF (VNA, S11, BW, rendement) : [`/tests/rf/`](tests/rf/)  
- Fonctionnels (LoRa, GPS, Wi-Fi) : [`/tests/functional/`](tests/functional/)  
- Rapports et logs : [`/tests/reports/`](tests/reports/)  

---

## CI/CD
Workflows dans [`/ci/workflows/`](ci/workflows/) :
- `drc_erc.yml` : vérification ERC/DRC KiCad.  
- `firmware_build.yml` : build & lint firmware.  
- `export_gerbers.yml` : artefacts Gerbers + BOM.  
- `tests.yml` : exécution scripts Python (mesures/tests).  

---

## Licences & conformité
- [MIT License](LICENSE)  
- [Contributing guidelines](CONTRIBUTING.md)  
- [Changelog](CHANGELOG.md)  
- [AI Sources (usage IA documenté)](AI_SOURCES.md)  

---

Équipe HF-Project — projet académique RF/embedded 2025.
