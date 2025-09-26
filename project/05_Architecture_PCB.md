# Architecture technique & règles de conception PCB

---

## Schéma fonctionnel

```
[ Batterie 2S ] → [ BQ25798 PMIC ] → [ ESP32-C3/S6 ]
                                   ↘ SPI → [ LoRa RFM95 ]
                                   ↘ UART → [ GPS AM-M8Q-0 ]
USB-C ──► Prog/Charge
SMA ──► Antenne 868 MHz (PCB séparée)
Wi-Fi/BLE ──► Antenne intégrée ESP32
```

---

## Partition du système
- **Carte embarquée** : ESP32, GPS, LoRa, PMIC, USB-C, connectique.
- **Carte antenne dédiée** : antenne PCB 868 MHz (FR4, 2 couches), reliée par SMA.
- **Firmware** : drivers GPS/LoRa/PMIC + démos Wi-Fi/BLE/LoRa/GPS.
- **Interfaces de test** : UART debug, points de mesure, connecteurs alim.

---

## Stack-up PCB
- **FR4 standard 2 couches (JLCPCB)**, épaisseur 1.6 mm, cuivre 35 µm.
- **Carte embarquée** : routage mixte digital + RF (LoRa, USB).
- **Carte antenne** : antenne + réseau d’adaptation π-LC, microstrip 50 Ω.

---

## Budget RF
- **Perte FR4 @868 MHz** : ~0.2 dB/cm (trace microstrip 1.6 mm).
- **Lignes RF** : ≤ 3 cm max entre RFM95 et SMA.
- **Connecteur SMA** : VSWR ≤ 1.2.
- **Matching** : S11 < –10 dB @868 MHz, BW ≥ 2 MHz.

---

## Règles de conception PCB
- **Plans de masse** : continus, sans coupure sous RF.
- **Vias de garde** : tous les 5 mm autour des lignes RF.
- **Lignes RF** : microstrip 50 Ω calculées (AppCAD/Qucs).
- **Retours de courant** : via stitching aux transitions.
- **Découplage** : 100 nF + 1 µF + 10 µF proches VCC, self ferrite pour RF.
- **Isolation** : cloisons cuivre (guard traces) entre GPS et LoRa.
- **USB** : paires différentielles, longueur identique ±0.5 mm, Zdiff = 90 Ω.

---

## Checklist JLCPCB (2 couches)
- Largeur min piste : 6 mil (0.152 mm).
- Espacement min piste : 6 mil.
- Via min : 0.3 mm drill / 0.6 mm pad.
- Annular ring ≥ 0.15 mm.
- Taille pad min : 0.25 mm.
- Clearances > 0.2 mm.
- Trous métallisés seulement (pas de via-in-pad sur ce POC).

---

## Contrôles qualité
- **ERC/DRC** : zéro erreur bloquante.
- **DFM** : respect règles JLCPCB.
- **Revue pair** : validation schéma/routage par un second membre.
- **Checklists** : intégrées dans CI (ERC/DRC headless).
