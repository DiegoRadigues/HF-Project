# Organisation du repo GitHub

Ce document décrit la structure du dépôt **HF-Project**, les conventions de travail, et les outils CI/CD utilisés.  
Il sert de référence pour l’équipe et doit être maintenu à jour au fil du projet.

---

## 1. Branches Git

- `main` → branche stable, **toujours compilable et testée**.  
- `dev` → intégration continue, PR mergeables uniquement après review et CI verte.  
- `feature/<slug>` → développement d’une fonctionnalité (ex. `feature/lora-driver`).  
- `fix/<slug>` → corrections rapides (ex. `fix/usb-footprint`).  
- `docs/<slug>` → documentation (ex. `docs/quickstart-v1`).  

**Règles :**
- Les PR vont de `feature/*` → `dev`, puis `dev` → `main`.  
- Pas de commit direct sur `main`.  
- Historique propre : squash & merge recommandé.  

---

## 2. Conventions de commit

Format : **[Conventional Commits](https://www.conventionalcommits.org/fr/v1.0.0/)**  

```
<type>(scope): résumé court
```

Types : `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `ci`, `chore`, `hw`, `fw`.  

Exemples :  
- `feat(fw): ajout driver LoRa RFM95`  
- `hw(pcb): correction footprint USB-C`  
- `ci(kicad): ajout DRC/ERC headless workflow`  

---

## 3. Arborescence du dépôt

```
HF-Project/
├── project/              # Plan de projet (01–10)
├── docs/                 # Documentation utilisateur
│   ├── datasheet/        # Fiche produit
│   ├── quickstart/       # Guide de démarrage
│   ├── tutorials/        # Tutoriels pratiques
│   ├── report/           # Rapport final
│   └── slides/           # Présentation orale
├── hardware/             # Schémas, PCB, antenne
│   ├── kicad/            # Projet KiCad + règles JLCPCB
│   ├── fabrication/      # Gerbers, BOM, Pick&Place
│   ├── antenna/          # Design antenne (OpenEMS, Qucs, résultats)
│   └── emi_cem/          # Plans et rapports EMI/CEM
├── firmware/             # ESP32 + outils
│   ├── esp32/            # Drivers, exemples
│   └── tools/            # Scripts Python de test
├── tests/                # Protocoles et résultats de tests
│   ├── rf/               # Plans VNA, scripts SCPI
│   ├── functional/       # LoRa, GPS, Wi-Fi
│   └── reports/          # Résultats labo & instrumentés
├── logs/                 # Journal de bord
│   ├── journal/          # YYYY-MM-DD.md
│   ├── journal_index.md  # Index des logs
│   └── journal_template.md
├── ci/                   # Workflows GitHub Actions
│   └── workflows/        # drc_erc.yml, firmware_build.yml, etc.
├── .github/              # Templates PR, issues
├── README.md             # Présentation projet
├── CONTRIBUTING.md       # Guide de contribution
├── CHANGELOG.md          # Historique des versions
├── LICENSE               # Licence MIT
└── AI_SOURCES.md         # Usage d’outils IA
```

---

## 4. Workflows CI/CD

Présents dans `/ci/workflows/` :  
- `drc_erc.yml` → vérification DRC/ERC KiCad.  
- `export_gerbers.yml` → export automatique Gerbers + BOM.  
- `firmware_build.yml` → compilation ESP32 + lint.  
- `tests.yml` → exécution des scripts de tests RF/functional.  

> Objectif : **une PR ne peut être mergée que si tous les jobs passent.**

---

## 5. Documentation associée

- [CONTRIBUTING.md](../CONTRIBUTING.md) → conventions branches, commits, règles HW/FW.  
- [CHANGELOG.md](../CHANGELOG.md) → suivi des évolutions versionnées.  
- [PROJECT_PLAN.md](../PROJECT_PLAN.md) → vue d’ensemble des livrables.

---

## 6. Bonnes pratiques

- Toujours associer les commits à des issues GitHub (`Fixes #id`, `Refs #id`).  
- Nommer clairement les fichiers et répertoires.  
- Garder une cohérence UTF-8 + LF (contrôlé par `.editorconfig`).  
- Faire vivre ce fichier `09_Repo_GitHub.md` en même temps que l’évolution du repo.  
