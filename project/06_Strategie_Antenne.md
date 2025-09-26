# Stratégie antenne 868 MHz

---

## Choix du type d’antenne
- **Type retenu** : Inverted-F Antenna (IFA) sur PCB.  
- **Justification** :
  - Compatible avec dimensions max 10×10 cm (FR4, 2 couches).
  - Rendement correct (≥ 50 %) avec surface réduite.
  - Accordable facilement via longueur effective et réseau π-LC.
  - Implémentation robuste (moins sensible à la main/boîtier qu’un monopole simple).

---

## Critères de sélection
- Bande : 863–870 MHz (LoRa EU868).
- Accord : S11 < –10 dB @ 868 MHz.
- Bande passante : ≥ 2 MHz (compat LoRa).
- Rendement visé : ≥ 50 %.
- Taille max : < 8 cm de longueur effective sur PCB.
- Fabricable en FR4 standard (1.6 mm).

---

## Procédure de conception & simulation

1. **Modélisation initiale**
   - Implémenter une IFA sur plan de masse FR4 (εr = 4.4, h = 1.6 mm).
   - Utiliser **OpenEMS** pour simuler S11.
   - Paramètres variables : longueur bras rayonnant, largeur piste, gap feed.

2. **Optimisation**
   - Sweep longueur (λ/4 ≈ 8.6 cm @868 MHz).
   - Ajuster feed + stub pour minimiser S11.
   - Objectif : S11 < –10 dB centré sur 868 MHz.

3. **Adaptation**
   - Exporter S-param (Touchstone `.s1p`).
   - Importer dans **Qucs** pour concevoir réseau π-LC.
   - BOM : inductances Murata LQW, capas GRM, valeurs standard série E12.

4. **Fabrication**
   - Exporter Gerbers antenne seule (PCB séparé).
   - Ajout connecteur SMA femelle edge-mount.

---

## Protocole de caractérisation

### Instrumentation
- **VNA** (100 kHz – 3 GHz).
- **Calibration** : SOLT (Short, Open, Load, Through).
- **Câble coax** calibré avec adaptateur SMA.

### Mesures
1. **S11** :
   - Mesurer 800–950 MHz.
   - Attendu : min S11 < –10 dB @ 868 MHz.
2. **Bande passante** :
   - Largeur à –10 dB ≥ 2 MHz.
3. **Rendement** :
   - Méthode champ proche → champ lointain (si équipement dispo).
   - Sinon, comparer RSSI LoRa en champ libre avec antenne de réf.
4. **Diagramme de rayonnement** (optionnel) :
   - Mesure rotationnelle (0–360°) en chambre ou en extérieur.

### Logs attendus
- `s11_meas.csv` : S11 mesuré.
- `antenna_bw.png` : courbe bande passante.
- `efficiency_report.md` : rendement et commentaire.
- `range_test.log` : portée LoRa terrain.

---

## Résultats attendus
- Antenne fonctionnelle accordée à 868 MHz.
- Simulations cohérentes avec mesures (< ±5 MHz de décalage).
- Documentation claire : design → simu → fabrication → mesure.
