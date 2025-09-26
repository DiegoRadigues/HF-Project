# Planning & jalons (Gantt simplifié)

Le planning est aligné sur les 6 phases définies dans le projet.  
Chaque phase comprend un livrable, une marge de risque, et un point de contrôle.  
Les réunions « client–developer » de 10 min ouvrent chaque séance pour suivi/notation continue.

---

## Vue Gantt simplifiée

| Phase | Semaines (indicatif) | Jalons livrables | Points de contrôle | Marge risque |
|-------|----------------------|------------------|--------------------|--------------|
| **P1 — PCB Implémentation** | S2 → S5 (due 19/10) | Gerbers + BOM validée | Revue ERC/DRC, vérif JLCPCB rules | +1 sem (fab PCB) |
| **P2 — Software & antenne choix** | S6 (due 26/10) | Firmware stub (UART log, Wi-Fi scan) + choix type antenne | Démo scan Wi-Fi en labo | buffer 2j |
| **P3 — Antenne design & simu** | S7 → S9 (due 23/11) | Design OpenEMS/Qucs + Gerbers antenne PCB | Revue plots S11 | +1 sem (optimisation) |
| **P4 — Protocoles & pré-tests** | S9 → S10 (due 30/11) | Protocoles test RF, pré-scan EMI/CEM | Dry-run VNA (calibration) | buffer 3j |
| **P5 — Tests instrumentés** | S10 → S12 (due 14/12) | Résultats VNA, spectre, portée LoRa, GPS TTFF | Validation intégrée HW+SW | +1 sem (retard instruments) |
| **P6 — Oral final** | S13 (18/12) | Rapport final + slides + démo POC | Répétition générale | buffer 2j |

---

## Points de contrôle réguliers
- **Réunions client-développeur** : 10 min début de séance (feedback + note continue).
- **Mid-phase reviews** : check-list DRC/DFM (phase 1), test logs firmware (phase 2), S11 plots (phase 3).
- **Pré-oraux** : dry-run présentation et démo (phase 6-1 semaine).

---

## Livrables principaux
- **Phase 1** : PCB conforme (Gerbers, BOM, Pick&Place).
- **Phase 2** : Firmware minimal + antenne choisie.
- **Phase 3** : Design et simu antenne LoRa.
- **Phase 4** : Protocoles de test et pré-scan EMI/CEM.
- **Phase 5** : Résultats instrumentés (VNA, spectre, portée, GPS).
- **Phase 6** : Rapport complet + présentation + démo intégrée.
