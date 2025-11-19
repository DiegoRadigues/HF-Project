# HF-Project

Proof of Concept (POC) industriel : conception d’une solution RF sur PCB intégrant **ESP32, GPS, LoRa 868 MHz et une antenne dédiée**, avec **simulation, implémentation et caractérisation**.

---

## Objectifs
- Démontrer une chaîne **hardware + software fonctionnelle** :
  - Carte embarquée (ESP32, GPS, LoRa, PMIC, USB-C).
  - Carte antenne PCB 868 MHz conçue, simulée et caractérisée.
  - Firmware de démonstration : LoRa ping/pong, GPS NMEA, Wi-Fi/BLE scan.
- Fournir une documentation **style carte de développement** (datasheet, quickstart, tutoriels).
- Tenir un **journal de bord continu** servant de base au rapport final.

---

## Livrables officiels (évalués)

Les phases du projet suivent la grille imposée, chaque livrable est noté.

1. **PCB embarqué (Phase 1) 19oct25**
   - Carte ESP32 + GPS + LoRa + PMIC + USB-C  
   - Fichiers de fabrication : [Gerbers](hardware/fabrication/Gerbers/), [BOM.csv](hardware/fabrication/BOM.csv), [Pick&Place.csv](hardware/fabrication/PickPlace.csv)

2. **Software & Lab concept (Phase 2)**
   - Firmware minimal : [`/firmware/esp32/`](firmware/esp32/)  
   - Premiers résultats labo : [`/tests/reports/lab_concept/`](tests/reports/lab_concept/)  
   - Choix de l’antenne : [Stratégie antenne](project/06_Strategie_Antenne.md)

3. **Antenne 868 MHz (Phase 3)**
   - Design simulé : [`/hardware/antenna/openems/`](hardware/antenna/openems/), [`/hardware/antenna/qucs/`](hardware/antenna/qucs/)  
   - Résultats S11 : [`s11_sim.csv`](hardware/antenna/results/s11_sim.csv)  
   - PCB antenne dédié : [`/hardware/antenna/`](hardware/antenna/)

4. **Protocoles & tests (Phase 4)**
   - Protocole VNA : [`plan_vna.md`](tests/rf/plan_vna.md)  
   - Pré-scan EMI/CEM : [`pre_scan_plan.md`](hardware/emi_cem/pre_scan_plan.md)  
   - Protocoles fonctionnels : [`protocoles.md`](tests/functional/protocoles.md)

5. **Tests instrumentés (Phase 5)**
   - S11 mesuré : [`s11_meas.csv`](tests/reports/instrumented/s11_meas.csv)  
   - Rapports de mesures : [`/tests/reports/instrumented/`](tests/reports/instrumented/)

6. **Examen oral & rapport (Phase 6)**
   - Présentation : [`/docs/slides/`](docs/slides/)  
   - Rapport final : [`Rapport_Final.md`](docs/report/Rapport_Final.md)


---

## Livrables internes (organisation & suivi)
Ces documents structurent le projet et préparent le rapport.

- [Project Plan complet](PROJECT_PLAN.md)  
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

- `/project/` → plan de projet (sections 01–10)  
- `/docs/` → documentation utilisateur (datasheet, quickstart, tutoriels, images)  
- `/hardware/` → schémas KiCad, Gerbers, antenne, EMI/CEM  
- `/firmware/` → drivers ESP32 + exemples  
- `/tests/` → plans, scripts et rapports de tests  
- `/logs/` → journal de bord continu  
- `/ci/` → workflows CI/CD  
- `/.github/` → templates Issues & PR  

---

## Journal de bord
- [Index du journal](logs/journal_index.md)  
- Journaux individuels : `logs/journal/YYYY-MM-DD.md`  

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
- Antenne 868 MHz : [`/hardware/antenna/`](hardware/antenna/)  

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
- `drc_erc.yml` → vérification ERC/DRC KiCad  
- `firmware_build.yml` → build & lint firmware  
- `export_gerbers.yml` → artefacts Gerbers + BOM  
- `tests.yml` → exécution scripts Python  

---

## Licences & conformité
- [MIT License](LICENSE)  
- [Contributing guidelines](CONTRIBUTING.md)  
- [Changelog](CHANGELOG.md)  
- [AI Sources (usage IA documenté)](AI_SOURCES.md)  

---


