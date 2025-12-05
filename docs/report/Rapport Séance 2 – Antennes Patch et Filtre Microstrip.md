# Laboratoire sur les hyperfréquences
## Partie 2 - Antennes Patch

### 1.1 Antenne de Référence — Patch Carré Adapté (L = 3,5 cm)

#### Paramètres de Base

| Paramètre | Valeur |
|-----------|--------|
| Permittivité relative | εᵣ = 3 |
| Hauteur du substrat | H = 0,5 mm |
| Côté du patch | L = 3,5 cm |
| Adaptation | Transformateur λ/4 (L₁, L₂) |

#### Analyse Théorique

Pour une antenne patch carrée, la condition de résonance est :

$$L \approx \frac{\lambda}{2}$$

La fréquence de résonance en première approximation vaut :

$$f_0 = \frac{c}{2L\sqrt{\varepsilon_r}}$$

Avec les valeurs données (L = 0,035 m, εᵣ = 3) :

$$f_0 \approx \frac{3 \times 10^8}{2 \times 0,035 \times \sqrt{3}} \approx 2,5 \text{ GHz}$$

**Attentes théoriques :**
- L'antenne doit rayonner efficacement autour de **2,5 GHz**
- Avec une adaptation quart d'onde idéale on attend un **minimum marqué de S₁₁** entre –10 et –15 dB à cette fréquence
- Des modes supérieurs vers 5 GHz, 7,5 GHz, etc., avec des minima moins pertinents

#### Résultats observés en simulation

<img width="600" height="395" alt="LAB2_1 1 1" src="https://github.com/user-attachments/assets/b0acbe5c-cc0d-4ef4-aad9-9b08d879a834" />



Sur le graphe S₁₁ :
- Présence d'une série de creux régulièrement espacés en fréquence
- À 2,5 GHz : $$S_{11} \approx -5,8 \text{ dB}$$
- Minima plus profonds (> –20 dB) observés au-delà de 30 GHz

**Interprétation :** La résonance correspond avec nos attentes mais l'adaptation est **moins bonne que prévu** (–5,8 dB au lieu de –10 dB). 26,3% de la puissance est réflechie

#### Écarts Théorie/Simulation — Hypothèses

| Hypothèse | Explication |
|-----------|-------------|
| **Adaptation λ/4 imparfaite** | L'impédance réelle du patch ne coïncide pas exactement avec celle utilisée pour le calcul du transformateur. L'adaptation à 50 Ω n'est donc pas idéale. |
| **Modélisation simplifiée (fringing fields)** | La formule ne tient pas compte de la permittivité effective εₑff et de l'allongement électrique ΔL. L'impédance réelle et la fréquence dévient donc des prédictions. |
| **Résonances de la structure complète** | Les segments L₁, L₂ et l'antenne forment une ligne composite qui, à haute fréquence, devient multi-λ/2, générant les multiples creux de S₁₁ observés. |
| **Pertes dans substrat/conducteur** | Les pertes (TanD = 0,001) réduisent le facteur Q, ce qui produit un creux moins profond. |
| **Résolution fréquentielle (0,1 GHz)** | Le vrai minimum peut se trouver entre deux points d'échantillonnage et être plus profond que le –5,8 dB affiché. |


---

### 1.2 Antenne patch avec une mauvaise adaptation d’antenne

#### Caractéristiques

Configuration identique à l'antenne de référence sauf absence du transformateur λ/4

#### Analyse Théorique

La fréquence de résonance structurelle reste la même :

$$f_0 \approx 2,5 \text{ GHz}$$

**Attentes :**
- Absence d'adaptation → très fortes réflexions → S₁₁ proche de 0 dB à la résonance
- L'antenne rayonnera très peu malgré la présence structurelle d'une résonance
- Modes supérieurs plus visibles en raison des multiples résonances de ligne

#### Résultats observés

<img width="600" height="407" alt="LAB2_1 1 2" src="https://github.com/user-attachments/assets/cd532e2f-a1c3-41de-977e-f4b0fb149003" />


À 2,5 GHz :
- $$S_{11}(2,5 \text{ GHz}) \approx -1,25 \text{ dB}$$
- La plupart de la puissance est réfléchie (75%)

**Autres observations :**
- Succession dense de creux très étroits, typiques d'une structure résonante mal adaptée
- Minima profonds (> –8 dB) seulement à haute fréquence (20–40 GHz)

#### Analyse des écarts

| Cause | Explication |
|-------|-------------|
| **Absence d'adaptation (cause principale)** | Sans λ/4, l'alimentation voit directement l'impédance du patch (~100–300 Ω). Le coefficient de réflexion est : $$\rho = \frac{Z_{in} - 50}{Z_{in} + 50}$$, d'où $$\|\rho\| \approx 0,7–0,9$$ → S₁₁ ≈ –1 à –3 dB |
| **Mauvais point d'alimentation** | Le feed direct au bord crée une impédance très élevée → désadaptation maximale |
| **Résonances internes** | Les aller-retours d'énergie entre patch et source créent les multiples creux périodiques observés |
| **Modélisation microstrip simplifiée** | Effets d'εₑff et fringing ; très secondaire ici face au manque d'adaptation |

---

### 1.3 Antenne patch plus petite (L = 1,7 cm)

#### Paramètres

| Paramètre | Valeur |
|-----------|--------|
| Permittivité relative | εᵣ = 3 |
| Hauteur | H = 0,5 mm |
| Côté du patch | L = 1,7 cm |
| Adaptation | Transformateur λ/4 (L₁, L₂ fournis) |

#### Analyse théorique

Avec L réduite, la fréquence de résonance augmente proportionnellement :

$$f_0 = \frac{c}{2 \times 0,017 \times \sqrt{3}} \approx 5,1 \text{ GHz}$$

**Attentes :**
- Résonance fondamentale entre **5 et 5,2 GHz**
- Adaptation λ/4 → creux significatif de S₁₁ (–10 à –20 dB idéalement)
- Modes supérieurs vers 10, 15, 20 GHz, etc.

#### Résultats observés

<img width="600" height="465" alt="LAB2_1 1 3" src="https://github.com/user-attachments/assets/d18d7e91-584a-4b5b-8d89-9e6de60267ba" />


- Marqueur indique : $$S_{11}(5,2 \text{ GHz}) = -2,35 \text{ dB}$$
- La fréquence de résonance correspond parfaitement à la théorie (~5 GHz) 
- Adaptation médiocre : –2,35 dB → ~58 % de la puissance renvoyée
- Beaucoup de minima étroits à 20–40 GHz
- Le mode fondamental très peu marqué → rayonnement faible

#### Analyse des écarts

| Cause | Détails |
|-------|---------|
| **Adaptation du λ/4 non optimale** | Avec L réduit, l'impédance du patch augmente. Si la valeur estimée pour le transformateur est imprécise, l'adaptation se dégrade (–2,3 dB au lieu de –10 dB). |
| **Résonance plus sensible aux fringing fields** | Sur une petite antenne, l'importance relative des champs de frange augmente, modifiant εₑff et le point d'alimentation optimal. |
| **Réflexions internes amplifiées** | Sur une antenne compacte, les segments de ligne d'alimentation deviennent proportionnellement plus grands → réflexions plus fortes. |
| **Pertes diélectriques** | TanD = 0,001 réduit Q, aplatissant la résonance. |


---

### 1.4 Antenne avec substrat à permittivité élevée (εᵣ = 4,8)

#### Paramètres

| Paramètre | Valeur |
|-----------|--------|
| Permittivité relative | εᵣ = 4,8 |
| Hauteur | H = 0,5 mm |
| Côté du patch | L = 2,8 cm |
| Adaptation | Transformateur λ/4 (L₁ = 1,4 cm, L₂ = 1,7 cm) |
| Pertes diélectriques | TanD = 0,02 (très élevé) |

#### Analyse théorique

La fréquence attendue est :

$$f_0 = \frac{c}{2 \times 0,028 \times \sqrt{4,8}} \approx 2,45 \text{ GHz}$$

**Attentes :**
- Résonance autour de **2,45 GHz** 
- **Pertes très importantes** (TanD = 0,02) → résonance large et peu profonde

##### Observations

<img width="600" height="433" alt="LAB2_1 1 4" src="https://github.com/user-attachments/assets/27aeb5e9-e7e7-4fa6-bea7-907ce3f9d772" />


- faible -8,8dB vers **2,45 GHz**  
- creux plus profond vers **5 GHz** (mode supérieur)  
- courbe bruitée, instable  

##### Analyse et hypothèses

- pertes très élevées → mode fondamental amorti      
- structure compacte → réflexions multiples  

---

#### 2. Synthèse

| Antenne | f₀ théorique | f₀ observée | S₁₁ observé | Rayonnement | Remarque |
|---------|--------------|-------------|-------------|-------------|----------|
| 1 — Référence | 2,5 GHz | 2,5 GHz | –5,8 dB | Moyen | Adaptation λ/4 imparfaite |
| 2 — Sans adaptation | 2,5 GHz | 2,5 GHz | –1,25 dB | Très faible | Désadaptation totale |
| 3 — Petit patch | 5,1 GHz | 5,2 GHz | –2,35 dB | Faible | Mauvaise adaptation |
| 4 — εᵣ = 4,8 | 2,45 GHz | 2,45 GHz | –8,8 dB | Moyen | Pertes élevées, mode fondamental masqué |

---

