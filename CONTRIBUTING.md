# CONTRIBUTING.md

Merci de contribuer à **HF-Project**   
Ce document décrit **comment travailler proprement** sur le repo : branches, commits, PR, style, vérifications CI et règles spécifiques Hardware/Firmware/Docs.

---

## 1) Pré-requis
- **Git** récent
- **ESP-IDF** (ou Arduino IDE) pour firmware ESP32
- **Python 3.10+** (scripts outils)
- **KiCad 7+** pour la CAO
- Accès aux Actions GitHub (CI)

---

## 2) Flux Git (branches)

- `main` : stable, **toujours** buildable.  
- `dev` : intégration continue.  
- `feature/<slug>` : une fonctionnalité/tâche (ex. `feature/lora-ping`).  
- `fix/<slug>` : corrections (ex. `fix/usb-footprint`).  
- `docs/<slug>` : documentation (ex. `docs/datasheet-v1`).

```bash
git checkout -b feature/lora-ping origin/dev
# ... commits ...
git push -u origin feature/lora-ping
```

> Les PR se font **vers `dev`** (sauf hotfix critique → `main`).

---

## 3) Messages de commit (Conventional Commits)

Utiliser le format :

```
<type>(scope): résumé court
```

**Types** usuels : `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `ci`, `hw`, `fw`.  
**Exemples** :
- `feat(fw): add LoRa ping/pong demo`
- `hw(pcb): fix USB-C differential pair clearance`
- `ci(kicad): add headless ERC/DRC workflow`

> Un commit = une intention claire. Ajoute des **références issues** : `Refs #12` / `Fixes #34`.

---

## 4) Pull Requests (PR)

- Merge target : **`dev`**.  
- Remplir le **template PR** (description, tests, impacts).  
- **Checklist** avant demande de review :
  - [ ] CI **verte** (build firmware, ERC/DRC si applicable)
  - [ ] Lint/format ok (code + Markdown)
  - [ ] Tests/Logs fournis si pertinent
  - [ ] Docs mises à jour (/project, /docs) si besoin

- **Reviews** : au moins **1 reviewer** autre que l’auteur.  
- Squash & merge recommandé (historique propre).

---

## 5) Règles Hardware (KiCad)

- Utiliser le dossier `/hardware/kicad/` (projet, libs, 3D).  
- **Règles JLCPCB 2 couches** appliquées (fichier de règles inclus).  
- **Avant PR** :
  - [ ] ERC = **0 erreur** bloquante
  - [ ] DRC = **0 erreur** bloquante
  - [ ] Footprints connecteurs (SMA, USB-C) **revus à 2** (pair review)
  - [ ] Export **Gerbers/BOM/PnP** → `/hardware/fabrication/`

- Antenne 868 MHz : design + simu → `/hardware/antenna/`  
  - Fichiers OpenEMS/Qucs + résultats S11 (CSV/PNG)
  - Note de conception (paramètres, hypothèses, limites)

---

## 6) Règles Firmware (ESP32)

- Arborescence : `/firmware/esp32/` (ESP-IDF conseillé).  
- Style : **clang-format** (ou `idf.py clang-format` si dispo).  
- Logs : UART 115200, **pas de secrets** dans le repo.  
- **Avant PR** :
  - [ ] `idf.py build` **OK**
  - [ ] Lint/format **OK**
  - [ ] Exemples mis à jour si API change
  - [ ] Scripts outils dans `/firmware/tools/` documentés (`--help`)

---

## 7) Règles Tests & Mesures

- Scripts de mesure RF (SCPI/VNA) → `/tests/rf/`  
- Procédures fonctionnelles → `/tests/functional/`  
- Rapports et CSV/plots → `/tests/reports/`  
- **Nommage** : `YYYY-MM-DD_<module>_<test>.{md,csv,png}`  
- Joindre **méthode + setup** + **critères de réussite**.

---

## 8) Documentation

- Utiliser Markdown. Images dans `/docs/images/`.  
- Datasheet/Quickstart/Tutoriels → `/docs/`  
- Plan de projet → `/project/` (sections 01 → 10).  
- **Journal de bord** : `/logs/journal/YYYY-MM-DD.md` (utiliser le template).

---

## 9) CI/CD

- Actions GitHub dans `/ci/workflows/` :  
  - `drc_erc.yml` : vérifs KiCad headless  
  - `firmware_build.yml` : build + lint ESP-IDF  
  - `export_gerbers.yml` : artefacts fabrication  
  - `tests.yml` : exécution scripts Python (si applicable)

> Une PR doit passer **tous** les jobs pertinents.

---

## 10) Sécurité & conformité

- Pas de secrets/credentials en clair (utiliser variables GitHub).  
- Respect licences des libs/outils → ajouter dans `AI_SOURCES.md` et README si pertinent.  
- Données personnelles : anonymiser logs (GPS, Wi-Fi).

---

## 11) Comment démarrer (dev local)

```bash
# Cloner et créer la branche de feature
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

## 12) Code of Conduct (résumé)
- Bienveillance, respect, feedback constructif.  
- Les reviews portent sur le **code**, jamais sur les personnes.  
- Signale tout comportement inapproprié aux responsables du projet.

Merci ! 
