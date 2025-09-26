# Avancement du projet — HF-Project

Document de pilotage unique : état réel, gates par phase, DoD, orga GitHub/CI, liens vers livrables.

---

## 0) Organisation & GitHub
- [x] Branches : `main` (stable), `dev` (intégration), `feature/*`
- [x] Conventions : `.editorconfig`, `.gitattributes` (UTF-8 + LF)
- [x] Templates GitHub : issues (bug/feature/task), PR
- [ ] `CHANGELOG.md` (à démarrer dès la prochaine release)
- [x] Guide contribution : [CONTRIBUTING.md](CONTRIBUTING.md)
- [x] Licence : [MIT](LICENSE)

### CI/CD (doit passer en “non vide”)
- [ ] KiCad ERC/DRC headless : [/ci/workflows/drc_erc.yml](ci/workflows/drc_erc.yml)
- [ ] Export fabrication : [/ci/workflows/export_gerbers.yml](ci/workflows/export_gerbers.yml)
- [ ] Build ESP32 + lint : [/ci/workflows/firmware_build.yml](ci/workflows/firmware_build.yml)
- [ ] Tests Python/SCPI : [/ci/workflows/tests.yml](ci/workflows/tests.yml)

---

## 1) Definition of Done (DoD) — critères mesurables
- [ ] **LoRa portée** ≥ 300 m champ libre (PER < 5 %) — log : `/tests/reports/instrumented/`
- [ ] **Antenne** S11 < –10 dB @ 868 MHz — sim `/hardware/antenna/`, mesure `/tests/reports/instrumented/s11_meas.csv`
- [ ] **Rendement antenne** ≥ 50 % (estimation champ proche/lointain ou méthode comparative)
- [ ] **GPS TTFF** < 60 s en ciel dégagé — log : `/tests/reports/instrumented/`
- [ ] **Précision GPS** < 5 m (moyenne) — log : `/tests/reports/instrumented/`
- [ ] **Conso deep sleep (ESP32 seul)** < 20 µA — `/tests/reports/instrumented/`
- [ ] **EMI/CEM pré-scan** : aucun pic > –30 dBm (réf. EN 300 220) — `/hardware/emi_cem/`
- [ ] **Docs “dev board”** publiées : datasheet, quickstart, tutos — `/docs/`

---

## 2) Plan de projet (sections)
- [x] Vision & DoD — [01_Vision_DoD.md](project/01_Vision_DoD.md)
- [x] WBS & RACI — [02_WBS_RACI.md](project/02_WBS_RACI.md)
- [x] Planning & jalons — [03_Planning.md](project/03_Planning.md)
- [x] Plan de tests — [04_Tests.md](project/04_Tests.md)
- [x] Architecture PCB — [05_Architecture_PCB.md](project/05_Architecture_PCB.md)
- [x] Stratégie antenne — [06_Strategie_Antenne.md](project/06_Strategie_Antenne.md)
- [x] Validation HW/SW — [07_Validation_HW_SW.md](project/07_Validation_HW_SW.md)
- [x] Docs “dev board” — [08_Documentation_DevBoard.md](project/08_Documentation_DevBoard.md)
- [x] Repo GitHub — [09_Repo_GitHub.md](project/09_Repo_GitHub.md) 
- [x] Risques & qualité — [10_Risques_Qualite.md](project/10_Risques_Qualite.md)

---

## 3) Gates par phase (GO/NO-GO)

### Phase 1 — PCB embarqué (ESP32 + GPS + LoRa + PMIC + USB-C)
- [ ] Schémas validés (revue pair) — `/hardware/kicad/`
- [ ] ERC/DRC = 0 erreur bloquante (screenshot+rapport CI)
- [ ] Règles JLCPCB 2 couches respectées (checklist DFM)
- [ ] Gerbers exportés — `/hardware/fabrication/Gerbers/`
- [ ] BOM & Pick&Place — `/hardware/fabrication/`
- [ ] **Gate P1** : fabrication envoyée (bon de commande archivé)

### Phase 2 — Software & Lab concept
- [ ] Firmware minimal (UART, Wi-Fi scan, BLE scan) — `/firmware/esp32/`
- [ ] GPS NMEA lisible (log) — `/tests/reports/lab_concept/`
- [ ] LoRa ping/pong compile & échange — `/firmware/esp32/`
- [ ] Choix antenne justifié — `/hardware/antenna/README.md`
- [ ] **Gate P2** : démo labo + logs commités

### Phase 3 — Antenne 868 MHz (design + simu + PCB antenne)
- [ ] Modèle OpenEMS paramétré — `/hardware/antenna/openems/`
- [ ] Optimisation S11 < –10 dB @ 868 MHz — `/hardware/antenna/results/`
- [ ] Qucs : matching π/LC — `/hardware/antenna/qucs/`
- [ ] Gerbers antenne — `/hardware/fabrication/Gerbers/`
- [ ] **Gate P3** : dossier complet (simu + Gerbers) validé

### Phase 4 — Protocoles & pré-caractérisation (EMI/CEM inclus)
- [ ] Plan VNA + procédures — `/tests/rf/plan_vna.md`
- [ ] Pré-scan EMI/CEM — `/hardware/emi_cem/pre_scan_plan.md`
- [ ] Firmware test intégré (profil mesures) — `/firmware/esp32/`
- [ ] **Gate P4** : protocole relu + dry-run VNA

### Phase 5 — Tests instrumentés (VNA, spectre, scope) & validation intégrée
- [ ] S11 mesuré (CSV+plots) — `/tests/reports/instrumented/s11_meas.csv`
- [ ] Spectre RF, signaux horloge/PA (scope)
- [ ] Portée LoRa 300 m (PER < 5 %) — log terrain
- [ ] TTFF GPS < 60 s — log
- [ ] Conso deep sleep mesurée — CSV
- [ ] **Gate P5** : DoD atteint (ou plan d’actions)

### Phase 6 — Oral & rapport (basé sur le LOG)
- [ ] Slides — `/docs/slides/`
- [ ] Rapport final — `/docs/report/Rapport_Final.md`
- [ ] Journal consolidé — `/logs/journal_index.md`
- [ ] **Gate P6** : répétition générale + check matos démo

---

## 4) Documentation “dev board”
- [ ] Datasheet — [/docs/datasheet/Board_Datasheet.md](docs/datasheet/Board_Datasheet.md)
- [ ] Quickstart — [/docs/quickstart/Quickstart.md](docs/quickstart/Quickstart.md)
- [ ] Tutoriels (simu antenne, VNA, range test) — [/docs/tutorials/](docs/tutorials/)
- [ ] Mentions IA — [AI_SOURCES.md](AI_SOURCES.md)

---

## 5) Hardware & RF spécifiques
- [ ] `kicad/` (schéma, PCB, règles JLCPCB importées)
- [ ] `antenna/` (OpenEMS + Qucs + résultats S11)
- [ ] `emi_cem/` (modèle, pré-scan, rapport)

---

## 6) Firmware & outils
- [ ] `esp32/` (ESP-IDF projet, drivers RFM95, GPS AM-M8Q-0, PMIC BQ25798)
- [ ] `tools/` (scripts Python : SCPI VNA, post-traitement S-param)

---

## 7) Tests & rapports
- [ ] `tests/rf/` (plan VNA, scripts)
- [ ] `tests/functional/` (protocoles LoRa/GPS/Wi-Fi)
- [ ] `tests/reports/lab_concept/` (P2)
- [ ] `tests/reports/instrumented/` (P5)

---

## 8) Journal (notation continue)
- [x] Template — [/logs/journal_template.md](logs/journal_template.md)
- [ ] Index maintenu — [/logs/journal_index.md](logs/journal_index.md)

---

## 9) Risques & qualité
- [x] Registre des risques — [/project/10_Risques_Qualite.md](project/10_Risques_Qualite.md)
- [ ] Gates qualité cochés par phase (voir sections ci-dessus)
