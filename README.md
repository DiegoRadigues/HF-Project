# HF-Project

Proof of Concept (POC) industriel : conception dâ€™une solution RF sur PCB intÃ©grant ESP32, GPS, LoRa 868 MHz et une antenne dÃ©diÃ©e, avec simulation, implÃ©mentation et caractÃ©risation.

---

## Objectif
- DÃ©montrer une chaÃ®ne hardware + software fonctionnelle :
  - Carte embarquÃ©e (ESP32, GPS, LoRa, PMIC, USB-C).
  - Carte antenne PCB 868 MHz conÃ§ue, simulÃ©e et caractÃ©risÃ©e.
  - Firmware de dÃ©monstration : LoRa ping/pong, GPS NMEA, Wi-Fi/BLE scan.
- Fournir une documentation style carte de dÃ©veloppement (datasheet, quickstart, tutoriels).
- Tenir un journal de bord continu servant de base au rapport final.

---

## Plan de projet
Le projet est dÃ©coupÃ© en 6 phases, chacune avec livrables.

- [Project Plan complet](PROJECT_PLAN.md)
- Sections dÃ©taillÃ©es :
  1. [Vision & DoD](project/01_Vision_DoD.md)  
  2. [WBS & RACI](project/02_WBS_RACI.md)  
  3. [Planning & jalons](project/03_Planning.md)  
  4. [Plan de tests](project/04_Tests.md)  
  5. [Architecture PCB](project/05_Architecture_PCB.md)  
  6. [StratÃ©gie antenne](project/06_Strategie_Antenne.md)  
  7. [Validation HW/SW](project/07_Validation_HW_SW.md)  
  8. [Docs Â« dev board Â»](project/08_Documentation_DevBoard.md)  
  9. [Repo GitHub](project/09_Repo_GitHub.md)  
  10. [Risques & qualitÃ©](project/10_Risques_Qualite.md)

---

## Structure du repo

- `/project/` â†’ plan de projet (sections 01â€“10).  
- `/docs/` â†’ documentation utilisateur (datasheet, quickstart, tutoriels, images).  
- `/hardware/` â†’ schÃ©mas KiCad, Gerbers, antenne, EMI/CEM.  
- `/firmware/` â†’ drivers ESP32 + exemples.  
- `/tests/` â†’ plans, scripts et rapports de tests.  
- `/logs/` â†’ journal de bord (suivi continu).  
- `/ci/` â†’ workflows CI/CD.  
- `/.github/` â†’ templates issues/PR.  

---

## Journal de bord
- [Index du journal](logs/journal_index.md)  
- Journaux individuels : `/logs/journal/YYYY-MM-DD.md`

---

## Documentation
- [Datasheet (Ã  complÃ©ter)](docs/datasheet/)  
- [Quickstart (flash, premiers tests)](docs/quickstart/)  
- [Tutoriels pratiques](docs/tutorials/)  

---

## DÃ©veloppement

### Hardware
- SchÃ©mas et PCB : [`/hardware/kicad/`](hardware/kicad/)  
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
- `drc_erc.yml` : vÃ©rification ERC/DRC KiCad.  
- `firmware_build.yml` : build & lint firmware.  
- `export_gerbers.yml` : artefacts Gerbers + BOM.  
- `tests.yml` : exÃ©cution scripts Python (mesures/tests).  

---

## Licences & conformitÃ©
- [MIT License](LICENSE)  
- [Contributing guidelines](CONTRIBUTING.md)  
- [Changelog](CHANGELOG.md)  
- [AI Sources (usage IA documentÃ©)](AI_SOURCES.md)  

---

Ã‰quipe HF-Project â€” projet acadÃ©mique RF/embedded 2025.


