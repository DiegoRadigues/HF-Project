# Notes techniques – Antenne QFH 868 MHz

Possibilité d’une antenne **Quadrifilar Helix (QFH)** pour **868 MHz** basées sur :

- Le dépôt GitHub : *cernohorsky / QFH-Antenna-868MHz*
- Le calculateur QFH de John Coppens
- Les notes et simulations d’OH2GVB (helix2nec)

---


**Dimensions données dans le dépôt :**

- Fil cuivre argenté 0,8 mm  
- Boucle grande : **357 mm**  
- Boucle petite : **339,4 mm**  
- Câble d’alimentation : RG174 + SMA  

 **Note :**  
Le support imprimé ajoute une capacité parasite qui décale la fréquence de résonance.  
Le modèle est volontaire calculé fait pour **~913 MHz** afin que la résonance réelle tombe proche de **868 MHz**.

---

## Utilisation du calculateur QFH (JCoppens)

permet de définir :

- fréquence de conception  
- nombre de tours 
- périmètre (1 λ typiquement)  
- rayon de courbure  
- diamètre du conducteur  
- ratio hauteur/diamètre (0.3–0.44 classique)

Le calculateur fournit :

- longueurs de boucle compensées  
- séparations verticales/horizontales  
- hauteur totale de l’antenne  
- diamètre interne  
- modèle de perçage (gabarit PDF)

Générateur : *jcoppens.com/ant/qfh/calc*

---

## Direction de polarisation & alimentation (OH2GVB)

Deux paramètres déterminent la polarisation finale et le sens de radiation :

1. **Sens du twist** 
2. **Connexion au feedpoint** (standard /anti-standard)

Pour un feedpoint en haut :

| Twist | Connexion | Radiation | Polarisation |
|-------|-----------|-----------|--------------|
| gauche | standard | vers le haut | RHCP |
| droite | anti-standard | vers le haut | LHCP |
| gauche | anti-standard | vers le bas | RHCP |
| droite | standard | vers le bas | LHCP |

Pour du LoRa 868 MHz → **RHCP vers le haut**.

---

## Simulation NEC2 : helix2nec

OH2GVB fournit un générateur de modèles **NEC2** :

- entrée : dimensions (H, D, twist, rayon, diamètre fil…)  
- sortie : modèle NEC complet pour xnecview / nec2c  
- permet de vérifier :  
  - fréquence de résonance  
  - impédance  
  - patterns d’irradiation  
  - interaction entre hélices multiples

Commandes :

```
gcc -o helix2nec helix2nec.c -lm
helix2nec input.helix output.nec
nec2c -i output.nec -o simu.out
xnecview simu.out
```

---

## Effet indésirables supports 3D

Le support plastique :

- augmente la capacité parasite  
- décale la fréquence  
- peut nécessiter :
  - raccourcir les boucles  
  - changer le diamètre  
  - ajuster la position d’alimentation

Règle empirique observée :  
Prévoir **1–3 % de réduction** des longueurs finales.

---

## Conseils de construction

### Matériaux
- Cuivre argenté 0,8–1 mm  
- PLA/ABS ou PETG (éviter trop d’humidité → influence diélectrique)  
- Coax : RG174 ou RG316  

### Rigidité
- Les boucles doivent rester parfaitement symétriques.  
- Prévoir un mât central rigide pour éviter les torsions.

### Soudure & alimentation
- Limiter la longueur du coax non blindé  
- Protéger la jonction : thermorétractable, PVC, etc.

---

## Mesures types

- VNA (NanoVNA ou équivalent) → viser un **S11 < –10 dB** autour de 868 MHz  
- Vérifier :
  - résonance  
  - impédance proche de 50 Ω  
  - circularité (optionnel : analyseur de polarisation)

---

## Ref

- Dépôt original : *github.com/cernohorsky/QFH-Antenna-868MHz*  
- Calculateur QFH : *jcoppens.com/ant/qfh/calc*  
- Simulations OH2GVB : *uuki.kapsi.fi/qha_simul.html*  
- Modèle Thingiverse original : *thingiverse.com/thing:634205*

---
