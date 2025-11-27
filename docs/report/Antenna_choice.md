# Antenna choice :

## 1. Intro
Comment adapter une simulation eMerge de patch antenna initialement prévu pour une fréquence autour de 1.575 GHz vers une antenne patch optimisée pour LoRa à 868 MHz.  
Nous discuterons ici des choix de dimensions, de matériaux, de conditions de simulation et de stratégie de maillage nécessaires pour obtenir un fonctionnement correct sur cette bande.

---

## 2. Principes généraux du patch rectangulaire
La fréquence de résonance d’un patch rectangulaire est approximée par :

<img width="224" height="59" alt="Capture d&#39;écran 2025-11-17 005331" src="https://github.com/user-attachments/assets/eaa8349f-51a6-4509-b0ce-e167bff002bd" />


Pour passer de 1.575 GHz à 868 MHz, il faut multiplier la longueur du patch presque par 2(car la fréquence est presque divisée par 2).

---

## 3. Adaptation des dimensions principales

### 3.1 Nouveau dimensionnement
Avec un substrat FR4 (εr ≈ 4,4, h = 1,6 mm), une longueur approximative pour 868 MHz est :

<img width="219" height="66" alt="Capture d&#39;écran 2025-11-17 005957" src="https://github.com/user-attachments/assets/ddcb6a3e-fbd6-4d4e-911e-4bc2340dff3b" />

Soit 82.3 mm



### 3.2 Largeur du patch
La largeur augmente pour favoriser un meilleur rendement :

<img width="228" height="75" alt="Capture d&#39;écran 2025-11-17 010059" src="https://github.com/user-attachments/assets/7fced333-5067-4824-b756-88deee286e44" />

soit 105 mm


### 3.3 Substrat
LoRa étant bas débit mais nécessitant une bonne portée :
Un substrat épais augmente la bande passante,

Un compromis :
- **épaisseur ~1.6 mm**, 
- **εr ≈ 4.4**.

---

## 4. Adaptation du feed et de l’inset

Pour 868 MHz :
- la ligne d'alimentation doit être élargie car l’impédance microstrip évolue avec la fréquence,
- la profondeur d’inset doit être recalculée et viser +- 50 Ω.

On peut utiliser les formules de la ligne microstrip :

<img width="239" height="50" alt="Capture d&#39;écran 2025-11-17 010225" src="https://github.com/user-attachments/assets/2af84a45-7bd5-4008-a2f1-2dafc8dc7f12" />

4.1 Ligne microstrip 50 Ω sur FR4

L’impédance d’une ligne microstrip dépend de la largeur w, de l’épaisseur h et de εr.
Pour FR4, h = 1,6 mm, εr ≈ 4,4, on a ~50 Ω pour une largeur ~3,1 mm.

Largeur de la ligne d’alimentation choisie : 3,1 mm, alignée au centre du patch et prolongée jusqu’au bord du PCB pour la connexion SMA.

L’inset permet de prélever l’impédance correcte (~50 Ω) à l’intérieur du patch.
On vise une profondeur d’environ 0,3·Lpatch, ajustée ensuite par simulation.

Dimensions finales de l’encoche :

Profondeur : 24,8 mm ≈ 0,3 × 82,5 mm

Largeur totale de l’encoche : 21,1 mm

zones découpées gauche/droite : 9 mm

piste centrale (ligne) : 3,1 mm


---

## 5. Ajustements de simulation

### 5.1 Fréquence de balayage
Pour trouver la résonance, on a d’abord utilisé un balayage large :
0,7–1,1 GHz avec 61 points, puis on a recentré la validation autour de la bande 863–870 MHz

### 5.2 Taille de l’airbox
Au moins λ/4 de marge autour de l’antenne.  
<img width="258" height="57" alt="Capture d&#39;écran 2025-11-17 010533" src="https://github.com/user-attachments/assets/59c75cc0-8477-4ad3-9ca3-19cddc43f227" />

À 868 MHz, λ ≈ 34 cm → airbox ≈ 80–100 mm n’est plus suffisant.  
Il faut utiliser une sphère 200–250 mm.

### 5.3 Maillage
La résolution recommandée : 

<img width="152" height="50" alt="Maillage" src="https://github.com/user-attachments/assets/7ea60054-0535-494b-a41c-c1f47c646938" />


---

## 6. Radiation pattern attendu
Les antennes patch à 868 MHz présentent :
- un diagramme de type broadside (maximum normal au patch),
- un gain typique 5–7 dBi,
- une polarisation linéaire.

---

## 7. Résumé des nouveaux paramètres pour LoRa

| Élément | Valeur 868 MHz | 
|--------|------------------|
| Longueur patch | 82,5 mm |
| Largeur patch | 105 mm |
| Substrat (W/H) | 180x180 mm |
| Airbox | 220 mm |
| Ligne d’alim | 3.1 mm |
| Plage de fréquences | 0.7-1.1 GHz |

## 8. Simulation

<img width="1084" height="146" alt="Figure_6" src="https://github.com/user-attachments/assets/f5646545-fbe6-462f-9c0b-255707b5b266" />

<img width="1950" height="1108" alt="Figure_7" src="https://github.com/user-attachments/assets/f5828ba5-052e-495d-95e6-3e8f068b55b9" />

<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/270f53bf-654f-4ea9-86f4-29c51f279c9c" />

<img width="600" height="600" alt="Figure_2" src="https://github.com/user-attachments/assets/e5f228a4-39fd-4f31-96f8-6bff9f1bcdf6" />

<img width="640" height="480" alt="Figure_3" src="https://github.com/user-attachments/assets/9de70e0a-f6ec-42ef-aafc-c298c1ed9c02" />

<img width="640" height="480" alt="Figure_4" src="https://github.com/user-attachments/assets/5fd7e9d2-239e-4c88-b4f3-8aa2db34749e" />

