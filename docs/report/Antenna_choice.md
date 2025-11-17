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
En gardant un substrat de permittivité proche de 3.38 (type Rogers 4003C), une longueur approximative pour 868 MHz est :

<img width="219" height="66" alt="Capture d&#39;écran 2025-11-17 005957" src="https://github.com/user-attachments/assets/ddcb6a3e-fbd6-4d4e-911e-4bc2340dff3b" />

Soit 70 à 80 mm



### 3.2 Largeur du patch
La largeur augmente pour favoriser un meilleur rendement :

<img width="228" height="75" alt="Capture d&#39;écran 2025-11-17 010059" src="https://github.com/user-attachments/assets/7fced333-5067-4824-b756-88deee286e44" />

soit 90-100mm


### 3.3 Substrat
LoRa étant bas débit mais nécessitant une bonne portée :
Un substrat épais augmente la bande passante,

Un compromis :
- **épaisseur ~1.6 mm**, 
- **εr ≈ 3.3 à 4.4**.

---

## 4. Adaptation du feed et de l’inset

Le code exemple utilise un **inset feed symétrique**.  
Pour 868 MHz :
- la ligne d'alimentation doit être élargie car l’impédance microstrip évolue avec la fréquence,
- la profondeur d’inset doit être recalculée et viser +- 50 Ω.

On peut utiliser les formules de la ligne microstrip :

<img width="239" height="50" alt="Capture d&#39;écran 2025-11-17 010225" src="https://github.com/user-attachments/assets/2af84a45-7bd5-4008-a2f1-2dafc8dc7f12" />


Pour un substrat Rogers 4003C, 1.6 mm, largeur conductrice d'environ **3.5 à 4.5 mm** donne en général ~50 Ω.

---

## 5. Ajustements de simulation

### 5.1 Fréquence de balayage
Dans l’exemple : 1.55–1.60 GHz  
Pour LoRa : 840–900 MHz avec un maillage un peu large au début.

### 5.2 Taille de l’airbox
Au moins λ/4 de marge autour de l’antenne.  
<img width="258" height="57" alt="Capture d&#39;écran 2025-11-17 010533" src="https://github.com/user-attachments/assets/59c75cc0-8477-4ad3-9ca3-19cddc43f227" />

À 868 MHz, λ ≈ 34 cm → airbox ≈ 80–100 mm n’est plus suffisant.  
Il faut utiliser une sphère 200–250 mm.

### 5.3 Maillage
La résolution recommandée :  
≤ λ/10 / √εr, donc environ 5–7 mm maximum → un maillage moins dense qu’à 1.6 GHz.

---

## 6. Radiation pattern attendu
Les antennes patch à 868 MHz présentent :
- un diagramme de type broadside (maximum normal au patch),
- un gain typique 5–7 dBi,
- une polarisation linéaire.

---

## 7. Résumé des nouveaux paramètres pour LoRa

| Élément | Valeur d’origine | Valeur pour LoRa 868 MHz |
|--------|------------------|---------------------------|
| Longueur patch | 52 mm | 70–80 mm |
| Largeur patch | 53 mm | 90–100 mm |
| Substrat (W/H) | 100×100 mm | 150–200 mm |
| Airbox | 100 mm | 200–250 mm |
| Ligne d’alim | 3.2 mm | 3.5–4.5 mm |
| Plage de fréquences | 1.55–1.6 GHz | 0.84–0.90 GHz |




