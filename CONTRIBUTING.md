# CONTRIBUTING.md

Merci de contribuer Ã  **HF-Project**   
Ce document dÃ©crit **comment travailler proprement** sur le repo : branches, commits, PR, style, vÃ©rifications CI et rÃ¨gles spÃ©cifiques Hardware/Firmware/Docs.

---

## 1) PrÃ©-requis
- **Git** rÃ©cent
- **ESP-IDF** (ou Arduino IDE) pour firmware ESP32
- **Python 3.10+** (scripts outils)
- **KiCad 7+** pour la CAO
- AccÃ¨s aux Actions GitHub (CI)

---

## 2) Flux Git (branches)

- `main` : stable, **toujours** buildable.  
- `dev` : intÃ©gration continue.  
- `feature/<slug>` : une fonctionnalitÃ©/tÃ¢che (ex. `feature/lora-ping`).  
- `fix/<slug>` : corrections (ex. `fix/usb-footprint`).  
- `docs/<slug>` : documentation (ex. `docs/datasheet-v1`).

```bash
git checkout -b feature/lora-ping origin/dev
# ... commits ...
git push -u origin feature/lora-ping
```

> Les PR se font **vers `dev`** (sauf hotfix critique â†’ `main`).

---

## 3) Messages de commit (Conventional Commits)

Utiliser le format :

```
<type>(scope): rÃ©sumÃ© court
```

**Types** usuels : `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `ci`, `hw`, `fw`.  
**Exemples** :
- `feat(fw): add LoRa ping/pong demo`
- `hw(pcb): fix USB-C differential pair clearance`
- `ci(kicad): add headless ERC/DRC workflow`

> Un commit = une intention claire. Ajoute des **rÃ©fÃ©rences issues** : `Refs #12` / `Fixes #34`.

---

## 4) Pull Requests (PR)

- Merge target : **`dev`**.  
- Remplir le **template PR** (description, tests, impacts).  
- **Checklist** avant demande de review :
  - [ ] CI **verte** (build firmware, ERC/DRC si applicable)
  - [ ] Lint/format ok (code + Markdown)
  - [ ] Tests/Logs fournis si pertinent
  - [ ] Docs mises Ã  jour (/project, /docs) si besoin

- **Reviews** : au moins **1 reviewer** autre que lâ€™auteur.  
- Squash & merge recommandÃ© (historique propre).

---

## 5) RÃ¨gles Hardware (KiCad)

- Utiliser le dossier `/hardware/kicad/` (projet, libs, 3D).  
- **RÃ¨gles JLCPCB 2 couches** appliquÃ©es (fichier de rÃ¨gles inclus).  
- **Avant PR** :
  - [ ] ERC = **0 erreur** bloquante
  - [ ] DRC = **0 erreur** bloquante
  - [ ] Footprints connecteurs (SMA, USB-C) **revus Ã  2** (pair review)
  - [ ] Export **Gerbers/BOM/PnP** â†’ `/hardware/fabrication/`

- Antenne 868 MHz : design + simu â†’ `/hardware/antenna/`  
  - Fichiers OpenEMS/Qucs + rÃ©sultats S11 (CSV/PNG)
  - Note de conception (paramÃ¨tres, hypothÃ¨ses, limites)

---

## 6) RÃ¨gles Firmware (ESP32)

- Arborescence : `/firmware/esp32/` (ESP-IDF conseillÃ©).  
- Style : **clang-format** (ou `idf.py clang-format` si dispo).  
- Logs : UART 115200, **pas de secrets** dans le repo.  
- **Avant PR** :
  - [ ] `idf.py build` **OK**
  - [ ] Lint/format **OK**
  - [ ] Exemples mis Ã  jour si API change
  - [ ] Scripts outils dans `/firmware/tools/` documentÃ©s (`--help`)

---

## 7) RÃ¨gles Tests & Mesures

- Scripts de mesure RF (SCPI/VNA) â†’ `/tests/rf/`  
- ProcÃ©dures fonctionnelles â†’ `/tests/functional/`  
- Rapports et CSV/plots â†’ `/tests/reports/`  
- **Nommage** : `YYYY-MM-DD_<module>_<test>.{md,csv,png}`  
- Joindre **mÃ©thode + setup** + **critÃ¨res de rÃ©ussite**.

---

## 8) Documentation

- Utiliser Markdown. Images dans `/docs/images/`.  
- Datasheet/Quickstart/Tutoriels â†’ `/docs/`  
- Plan de projet â†’ `/project/` (sections 01 â†’ 10).  
- **Journal de bord** : `/logs/journal/YYYY-MM-DD.md` (utiliser le template).

---

## 9) CI/CD

- Actions GitHub dans `/ci/workflows/` :  
  - `drc_erc.yml` : vÃ©rifs KiCad headless  
  - `firmware_build.yml` : build + lint ESP-IDF  
  - `export_gerbers.yml` : artefacts fabrication  
  - `tests.yml` : exÃ©cution scripts Python (si applicable)

> Une PR doit passer **tous** les jobs pertinents.

---

## 10) SÃ©curitÃ© & conformitÃ©

- Pas de secrets/credentials en clair (utiliser variables GitHub).  
- Respect licences des libs/outils â†’ ajouter dans `AI_SOURCES.md` et README si pertinent.  
- DonnÃ©es personnelles : anonymiser logs (GPS, Wi-Fi).

---

## 11) Comment dÃ©marrer (dev local)

```bash
# Cloner et crÃ©er la branche de feature
git clone <repo-url>
cd HF-Project
git checkout -b feature/<slug> origin/dev

# Firmware (exemple ESP-IDF)
cd firmware/esp32
idf.py set-target esp32c3
idf.py build

# Scripts Python (tests)
cd ../../tests/rf
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
python measure_s11.py --help
```

---

## 12) Code of Conduct (rÃ©sumÃ©)
- Bienveillance, respect, feedback constructif.  
- Les reviews portent sur le **code**, jamais sur les personnes.  
- Signale tout comportement inappropriÃ© aux responsables du projet.

Merci ! 

