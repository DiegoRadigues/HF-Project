# Conception et Analyse des Filtres EMI


## Abstract

Ce rapport présente une analyse de la conception des filtres CEM  pour les alimentations à découpage et convertisseurs DC-DC. Il présente les fondamentaux des émissions conduites et rayonnées, les mécanismes de bruit en mode commun (MC) et mode différentiel (MD), et les topologies de filtrage passif. Inclue l'impact des éléments parasites, la stabilité système, les méthodologies de test avec réseau de stabilisation d'impédance de ligne (LISN) et les compromis de conception. Exemples concrets + normes internationales (CISPR 16, CISPR 17, CISPR 25, EN 55032) et références techniques.

**Mots-clés :** CEM, EMI, filtre CEM, mode commun, mode différentiel, LISN, convertisseur DC-DC, stabilité, émissions conduites, émissions rayonnées, CISPR, parasites.

---


## TABLE DES MATIÈRES

1. [INTRODUCTION](#1-introduction)  
2. [CADRE THÉORIQUE](#2-cadre-théorique)  
3. [RÉPONSES AUX 13 QUESTIONS](#3-réponses-aux-13-questions)  
4. [SYNTHÈSE ET CONCLUSION](#4-synthèse-et-conclusion)  
5. [BIBLIOGRAPHIE](#5-bibliographie)  
6. [ANNEXES](#6-annexes)

---

## 1. INTRODUCTION

### 1.1 Enjeux de la compatibilité électromagnétique

La compatibilité électromagnétique (CEM) est la capacité d'un équipement électronique à fonctionner correctement dans son environnement électromagnétique sans générer de perturbations nuisibles pour d'autres équipements[1]. Les interférences électromagnétiques sont importantes dans la conception électronique moderne, notamment avec l'augmentation des fréquences de commutation (>500 kHz) dans les alimentations à découpage et convertisseurs DC-DC[1].

### 1.2 Contexte industriel et normatif

Les organismes de normalisation internationaux (IEC, CISPR, FCC, IEEE) définissent des limites pour les émissions conduites et rayonnées[2][4][9]. Les principales normes applicables sont :

- **CISPR 16** : Spécifications des équipements de mesure et méthodes de test[5]
- **CISPR 22/32** : Limites pour équipements de traitement de l'information[11]
- **IEC 61000** : Famille de normes CEM génériques[3][9]
- **MIL-STD-461G** : Exigences militaires américaines[4][7]
- **DO-160G** : Standards avioniques[23][26]
- **FCC Part 15** : Réglementation américaine pour dispositifs RF[22]

### 1.3 Distinction émissions conduites vs rayonnées

Les émissions électromagnétiques se propagent selon deux modes principaux :

- **Émissions conduites** : Mesurées dans la bande 150 kHz – 30 MHz (typique), se propagent via les câbles d'alimentation et de signal[44][47]
- **Émissions rayonnées** : Mesurées au-delà de 30 MHz (selon normes), se propagent par couplage en champ proche/lointain[1][44]

La limite de 30 MHz s'explique par le rapport λ/2π : en dessous de 30 MHz (λ > 10 m), les dimensions des équipements sont petites devant la longueur d'onde, favorisant le couplage conductif[50].

---

## 2. CADRE THÉORIQUE

### 2.1 Sources de bruit et mécanismes de couplage

#### 2.1.1 Origines du bruit EMI

Dans les alimentations à découpage, les sources principales sont[1][24] :

1. **Commutations rapides (dV/dt, dI/dt)** : Génèrent des harmoniques jusqu'à plusieurs dizaines de MHz
2. **Résonances parasites** : Oscillations dues aux inductances/capacités parasites des composants et pistes PCB
3. **Effets non-linéaires** : Diodes à récupération inverse, saturation de magnétiques

**Équation caractéristique du bruit harmonique** (onde rectangulaire) :

$$ V_n(f) = \frac{2 V_{pk}}{\pi n} \cdot \text{sinc}\left(\frac{n \pi t_r}{T}\right) $$

où \(n\) est le rang harmonique, \(t_r\) le temps de montée, \(T\) la période[1].

#### 2.1.2 Chemins de couplage

Trois mécanismes fondamentaux[1][27] :

- **Couplage capacitif (dV/dt)** : Champ électrique → capacités parasites → courants de déplacement
- **Couplage inductif (dI/dt)** : Champ magnétique → inductances mutuelles → tensions induites  
- **Couplage par impédance commune** : Partage de masse/retour → injection de bruit

### 2.2 Mode commun (MC) et mode différentiel (MD)

#### 2.2.1 Définitions formelles

**Mode différentiel (DM)** : Courants circulant en sens opposés dans les conducteurs aller/retour, ne passant pas par la masse[1][24] :

$$ I_{DM} = \frac{I_L - I_N}{2}, \quad V_{DM} = V_L - V_N $$

**Mode commun (CM)** : Courants circulant dans le même sens dans tous les conducteurs actifs, retournant par la masse[1][24] :

$$ I_{CM} = \frac{I_L + I_N}{2}, \quad V_{CM} = \frac{V_L + V_N}{2} $$

#### 2.2.2 Origines distinctes

- **MD** : Lié au fonctionnement normal du circuit (fréquence de commutation fondamentale et harmoniques paires/impaires)[1]
- **CM** : Généré par capacités parasites vers masse (C_SW du nœud de commutation, transformateurs non parfaits)[24][27]

**Exemple quantitatif** : Dans un convertisseur Buck avec C_SW = 50 pF, V_in = 48 V, f_sw = 250 kHz (t_r = 100 ns), le courant CM crête est[24] :

$$
I_{CM} \approx C_{SW} \cdot \frac{dV}{dt} = 50 \times 10^{-12} \cdot \frac{48}{100 \times 10^{-9}} = 24 \text{ mA}
$$

#### 2.2.3 Conversion MD ↔ CM

Une dissymétrie d'impédance (câbles, PCB, composants) convertit partiellement un mode en l'autre[30][33]. Les capacités parasites vers châssis jouent un rôle central dans cette conversion[27][30].

### 2.3 Impédances source et charge

#### 2.3.1 Impédance de ligne normalisée (LISN)

La norme CISPR 16-1-2 définit l'impédance de ligne artificielle (LISN) présentant 50 Ω aux bornes DUT dans la bande 150 kHz – 30 MHz[43][46][49]. Configuration typique :

```
[Réseau] ──[50µH + 5Ω]──┬──[1µF]──[Masse]
                         │
                     [50Ω]──[EMI Receiver]
```

**Fonctions du LISN**[43][46] :
1. Isolation du bruit secteur
2. Impédance stabilisée 50 Ω
3. Point de mesure calibré
4. Protection récepteur EMI

**Impédances effectives** (vue du DUT)[1] :
- Mode différentiel : 100 Ω (2 × 50 Ω en série)
- Mode commun : 25 Ω (2 × 50 Ω en parallèle)

#### 2.3.2 Impédance d'entrée négative (convertisseurs)

Pour un convertisseur régulé de puissance constante[1] :

$$
R_{in} = -\frac{V_{in}^2}{\eta \cdot P_{out}}
$$

**Critère de stabilité système** : L'impédance de sortie du filtre doit satisfaire[1] :

$$
|Z_{out,filter}(j\omega)| < |R_{in,converter}| \quad \forall \omega
$$

Exemple : Flyback 100 W, η = 0.9, V_in = 18-32 V → R_in,min = 2.9 Ω à pleine charge[1].

---

## 3. RÉPONSES AUX 13 QUESTIONS

### Question 1 : Différence entre émissions conduites et rayonnées, importance pour les filtres EMI

#### 3.1.1 Distinction fondamentale

**Émissions conduites** : Perturbations HF propagées par les câbles/pistes de connexion, mesurées par tension/courant RF[44][47]. Bande typique : 150 kHz – 30 MHz (CISPR 22/32), 10 kHz – 10 MHz (MIL-STD-461 CE101)[2][4].

**Émissions rayonnées** : Couplage électromagnétique en espace libre (champ E, champ H), mesuré en intensité de champ (µV/m, dBµA/m)[1][44]. Bande typique : 30 MHz – 6 GHz (selon équipement)[2].

#### 3.1.2 Importance pour la conception des filtres

**Raison physique** : La transition 30 MHz correspond au changement de régime de propagation[50] :
- **< 30 MHz** : Dimensions équipement << λ → couplage dominant par câbles → filtres CEM efficaces
- **> 30 MHz** : Dimensions équipement ≈ λ → rayonnement direct → nécessité blindage + filtres

**Stratégie de filtrage**[1] :
1. Si émissions conduites maîtrisées → réduction automatique des rayonnées (source atténuée)
2. Filtres positionnés à la frontière environnement interne/externe (boîtier métallique)
3. Utilisation capacités traversantes (feedthrough) pour minimiser longueurs inductives parasites

### Question 2 : Bruit en mode commun (MC) et mode différentiel (MD) — Différences

#### 3.2.1 Définitions avec schéma de principe

```
Mode Différentiel (DM)          Mode Commun (CM)
      I_DM →                         I_CM →
L ────────→ [Charge]           L ──────────┐
                                            │ [C_parasites]
N ←──────── [Charge]           N ──────────┤ [C_parasites]
      I_DM                               I_CM ↓
                                         [Masse]
```

**Courants mesurés**[1][27] :
- DM : $\( I_{DM} = (I_L - I_N)/2 \)$ — circulation en boucle fermée L-N
- CM : $\( I_{CM} = (I_L + I_N)/2 \)$ — retour par masse via capacités parasites

#### 3.2.2 Origines et spectres associés

**Mode différentiel**[1][24] :
- Origine : Commutation du convertisseur (fondamentale f_sw + harmoniques)
- Spectre : Raies discrètes aux multiples de f_sw, décroissance en $\( f^{-2} \)$ (formes trapézoïdales)
- Bande typique : Dominant en basse fréquence (< 2 MHz)

**Mode commun**[1][24][27] :
- Origine : Capacités parasites du nœud de commutation vers masse (C_SW), couplage transformateur
- Spectre : Contenu haute fréquence dominant (dV/dt), comportement en sinc(f)/f
- Bande typique : Critique au-delà de 2 MHz

**Quantification exemple**[24] : Convertisseur Buck, C_SW variant de 50 pF à 200 pF → augmentation proportionnelle du bruit CM sur tout le spectre (mesure : +6 dB pour doublement).

### Question 3 : Nécessité de filtrer MC et MD simultanément

#### 3.3.1 Contribution spectrale complémentaire

Les mesures de séparation MD/CM montrent[1] :
- **150 kHz – 1 MHz** : Dominance MD (70-90% du bruit total)
- **1 MHz – 10 MHz** : Mixte (transition progressive vers CM)
- **> 10 MHz** : Dominance CM (60-80% du bruit)

**Conséquence** : Un filtre ne traitant qu'un seul mode échoue à supprimer les émissions sur toute la bande normative 150 kHz – 30 MHz[1][44].

#### 3.3.2 Conversion mode entre modes

Toute dissymétrie d'impédance (longueur câbles inégale, composants non appariés) convertit partiellement MD en CM et inversement[30][33]. Cette conversion non contrôlée exige un traitement bi-modal.

#### 3.3.3 Architecture filtre combinée

**Solution type** (circuit triphasé)[1] :

```
L_line ──[L_DM/2]──┬──[L_CM]──┬──[L_DM/2]── L_load
                   │          │
                 [X-cap]   [Y-cap]
                   │          │
N_line ──[L_DM/2]──┴──[L_CM]──┴──[L_DM/2]── N_load
                   │          │
                 [X-cap]   [Y-cap]
                                │
                             [Masse]
```

- **X-caps** (line-to-line) : Filtrage MD
- **Y-caps** (line-to-ground) : Filtrage CM
- **L_CM** (inductance de mode commun) : Haute impédance pour I_CM (typiquement 0.5 – 33 mH)[1]
- **L_DM** (inductance de fuite) : Impédance série pour I_DM (typiquement 1 – 5 µH)[1]

### Question 4 : Différence entre fonction de transfert/atténuation et perte d'insertion

#### 3.4.1 Atténuation (Transfer Function)

**Définition** : Rapport des tensions sortie/entrée sous conditions idéalisées[1] :

$$
A(f) = 20 \log_{10} \left| \frac{V_{out}(f)}{V_{in}(f)} \right|_{Z_S \to 0, Z_L \to \infty} \text{ [dB]}
$$

**Hypothèses** : Impédance source très basse, impédance charge très haute → fonction intrinsèque du filtre seul.

#### 3.4.2 Perte d'insertion (Insertion Loss)

**Définition normative** (CISPR 17)[1] :

$$
IL(f) = 20 \log_{10} \left| \frac{V_{L,no\_filter}(f)}{V_{L,with\_filter}(f)} \right| \text{ [dB]}
$$

**Procédure de mesure**[1] :
1. Mesurer tension/puissance charge sans filtre
2. Insérer filtre
3. Mesurer tension/puissance charge avec filtre
4. Calculer rapport logarithmique

**Dépendance aux impédances** : CISPR 17 exige mesures avec[1] :
- Configuration adaptée : Z_S = Z_L = 50 Ω
- Configuration désadaptée haute-Z : Z_S = 0.1 Ω, Z_L = 100 Ω (réaliste MD)
- Configuration désadaptée basse-Z : Z_S = 100 Ω, Z_L = 0.1 Ω (réaliste CM)

#### 3.4.3 Écart atténuation vs insertion loss

**Relation théorique** (filtre π, 2ème ordre)[1] :

$$
IL(f) = A(f) + 20\log_{10}\left|\frac{Z_S + Z_{in,filter}}{Z_S}\right| + 20\log_{10}\left|\frac{Z_L}{Z_L + Z_{out,filter}}\right|
$$

**Exemple mesuré**[1] : Filtre BMI316 (convertisseur 1 kW LLC, 48→12V) :
- Atténuation simulée @ f_sw = 1 MHz : 50 dB
- Insertion loss mesurée (EMI scan) : 27 dB
- Écart : 23 dB (dû aux désadaptations d'impédances réelles)

**Implications** :
- L'atténuation donne le comportement limite supérieur
- L'insertion loss reflète les performances réelles en environnement applicatif
- Conception prudente : viser atténuation > exigence normative + marge 6-10 dB[1]

### Question 5 : Composants typiques des filtres EMI et leurs rôles

#### 3.5.1 Inductances de mode différentiel (L_DM)

**Rôle** : Impédance série pour bloquer courants MD haute fréquence[1][42].

**Technologies courantes**[1] :
- Tores poudre de fer (MPP, High Flux) : Entrefer distribué, bonne linéarité jusqu'à 50 A
- Tores ferrite (NiZn) : Hautes perméabilités (µ_i = 1000-5000), saturation < 5 A
- Inductances à noyau C ou E : Conception avec gap pour DC, coût élevé

**Dimensionnement**[1] :

$$
L_{DM} = \frac{R_d}{2\pi F_0} \quad [\text{H}]
$$

où $\( R_d \)$ = impédance de conception (typ. 50 Ω), $\( F_0 \)$ = fréquence de coupure cible.

**Contrainte critique** : Éviter saturation par courant crête. Pour formes trapézoïdales (alimentations capacitives)[1] :

$$
I_{pk} = I_{RMS} \cdot \sqrt{\frac{2\pi}{\theta_{conduction}}}
$$

avec $\( \theta_{conduction} \)$ typiquement 30-60° → $\( I_{pk} \approx 4-5 \times I_{RMS} \)$.

#### 3.5.2 Inductances de mode commun (L_CM, "Zorro")

**Rôle** : Haute impédance pour I_CM, transparence pour I_DM[1][10].

**Principe** : Bobinage bifilaire sur tore — les flux MD s'annulent, les flux CM s'additionnent :

$$
L_{CM} = \frac{\mu_e N^2 A_e}{l_e} \quad [\text{H}]
$$

**Inductance de fuite** (inhérente)[1] :

$$
L_{leak} \approx 1-2\% \times L_{CM}
$$

Cette fuite contribue au filtrage MD (typ. 1-5 µH).

**Matériaux**[1] :
- Ferrites MnZn : µ_i = 5000-15000, f < 1 MHz
- Nanocristallins : Perméabilité stable en fréquence, faibles pertes, coût 3-5× ferrite

**Mesure caractéristique**[1] : Analyseur de réponse en fréquence (Omicron Bode 100), bobinages en parallèle (L_CM) ou série (L_leak).

#### 3.5.3 Condensateurs X (line-to-line)

**Rôle** : Shunt basse impédance pour courants MD haute fréquence[1][8].

**Types et limites**[1] :
- **Classe Y2/X2** (film polypropylène) : 250 VAC, ESR < 10 mΩ @ 100 kHz, SRF > 10 MHz
- **MLCC Classe 2 (X7R, X5R)** : Capacités élevées (4.7 – 10 µF), **dérating DC-bias critique**[1]

**Dérating DC-bias**[1] : MLCC 4.7 µF 100V X5R @ 48 VDC → capacité effective ≈ 0.47 µF (réduction 90%). **Vérification obligatoire** via courbes constructeur.

#### 3.5.4 Condensateurs Y (line-to-ground)

**Rôle** : Shunt courants CM vers masse[1][8].

**Contrainte sécuritaire** : Limitation courant de fuite terre (IEC 60950-1)[1] :

$$
I_{leakage} = \omega \cdot C_Y \cdot V_{line} < I_{max} \quad (typ. 0.75 - 3.5 mA)
$$

**Compensation** : Self de correction facteur puissance[1] :

$$
L_{PFC} = \frac{1}{\omega^2 C_{Y,total}}
$$

pour résonance série @ 50/60/400 Hz → courant circulant dans tank, pas vers terre.

**Classes de sécurité**[8] :
- Y1 : 250 VAC (isolation renforcée)
- Y2 : 150 VAC (isolation de base)

#### 3.5.5 Composants de damping (R-C, R-L)

**Problématique** : Filtres LC non amortis présentent facteur Q élevé → résonance, surtension, instabilité[1].

**Solution shunt R-C**[1] :

$$
R_d = R_{conception} \approx 50\, \Omega, \quad C_d = 4 \times C_{filter}
$$

Impédance $\( |Z_{RC}| \ll R_d \)$ à la fréquence de résonance → dissipation dans R_d, Q ≈ 1.

**Solution série R-L**[1] :

$$
L_d = 0.5 \times L_{filter}, \quad R_d = \omega_{pole} \cdot L_d
$$

Compromis : atténuation HF dégradée de facteur $\( L_{total}/(L_d \cdot L_{filter}) \)$ → compensation possible par sur-dimensionnement initial +9 dB[1].

### Question 6 : Effets des éléments parasites sur les performances

#### 3.6.1 Modèles de composants réels

**Inductance** (modèle équivalent)[1] :
```
DCR ──[L_ideal]──//──[C_parallel]
```
- **DCR** (résistance DC) : Pertes ohmiques, $\( R_{DC} = \rho \cdot l_{wire}/A_{wire} \)$
- **C_parallel** : Capacité inter-spires, détermine fréquence auto-résonance (SRF)

$$
f_{SRF,L} = \frac{1}{2\pi\sqrt{L \cdot C_{par}}}
$$

**Conséquence** : Au-delà de SRF, inductance devient capacitive → perte d'efficacité[1].

**Condensateur** (modèle équivalent)[1] :
```
ESR ──[ESL]──[C_ideal]
```
- **ESR** (résistance série équivalente) : Pertes diélectriques + résistance électrodes
- **ESL** (inductance série équivalente) : Connexions + structure interne

$$
f_{SRF,C} = \frac{1}{2\pi\sqrt{ESL \cdot C}}
$$

**Exemple mesuré**[1] : Morata 1 µF 100V X7R 0805 → ESR = 15 mΩ @ 100 kHz, ESL = 1.2 nH, SRF = 4.5 MHz.

#### 3.6.2 Impact sur réponse en fréquence

**Résonances parasites** : Interactions ESL-capacitance et C_parallel-inductance créent résonances série/parallèle non désirées[1].

**Atténuation multi-étages**[1] : Filtre π double avec composants non idéaux :
- Résonance série (ESL_C1 + L1) @ 3 MHz → pic +10 dB
- Résonance parallèle (C_par,L1 || C2) @ 8 MHz → creux -15 dB

**Stratégies d'atténuation**[1] :
1. **Sélection composants** : SRF > 5× fréquence maximale d'intérêt
2. **Parallélisation capacités** : MLCC haute valeur (basse SRF) + film faible valeur (haute SRF)
3. **Mise en quadrature inductances** : Orientation 90° pour minimiser couplage magnétique mutuel[1]

#### 3.6.3 Modélisation SPICE avancée

**Inductance de mode commun** (modèle 5 éléments)[1] :

$$
Z_{CM}(s) = \frac{R_1(s) + sL(s)}{1 + s^2L(s)C_{par}}
$$

où $\( L(s) \) et \( R_1(s) \)$ sont fonctions de fréquence (pertes magnétiques, skin effect).

**Validation expérimentale** : Analyseur impédance (ex: Omicron Bode 100), balayage 1 kHz – 50 MHz, comparaison module/phase[1].

### Question 7 : Impact du filtre EMI sur le système (stabilité, intégrité signal)

#### 3.7.1 Interaction avec convertisseur DC-DC

**Résistance d'entrée négative**[1] : Convertisseur régulé à puissance constante présente :

$$
\frac{dI_{in}}{dV_{in}} < 0 \quad \Rightarrow \quad R_{in,incremental} = \frac{\partial V_{in}}{\partial I_{in}} < 0
$$

**Critère de stabilité de Middlebrook**[1] :

$$
\left| \frac{Z_{out,filter}(j\omega)}{Z_{in,converter}(j\omega)} \right| < 1 \quad \forall \omega \in [f_{resonance}, f_{switching}]
$$

**Méthode graphique** : Tracé Bode $\( |Z_{out}| \) et \( |Z_{in}| \)$ — intersection ⇒ oscillation potentielle[1].

#### 3.7.2 Exemple de conception stable

**Cahier des charges**[1] : Flyback 100 W, V_in = 18-32 VDC, f_sw = 150 kHz, η = 0.9

$$
R_{in,min} = \frac{(18)^2}{0.9 \times 100} = 3.6\, \Omega
$$

**Filtre LC 2 pôles**[1] :
- $\( L = 190\, \mu H, C = 22\, \mu F \)$
- $\( f_{pole-Q} = 2.4\, kHz \)$
- $\( Z_{char} = \sqrt{L/C} = 2.9\, \Omega < R_{in,min} \)$

**Optimisation damping**[1] : Ajout R-C shunt $(\( R_d = 3\, \Omega, C_d = 88\, \mu F \))$ → réduction pic impédance de sortie de 4.5 dB, suppression surtension transitoire (15V → 6V).

#### 3.7.3 Effets sur intégrité du signal

**Affaiblissement signal utile** : Fréquence de coupure filtre trop proche de fréquence fondamentale alimentation (50/60/400 Hz) → chute tension, distorsion forme d'onde[1].

**Règle empirique**[1] :

$$
F_{0,filter} \geq 15 \times f_{line} \quad (ex: F_0 > 6\, kHz pour 400 Hz)
$$

**Courants de fuite capacitifs** : Y-caps injectent courant AC sur masse protectrice → contraintes IEC 60950-1 pour sécurité utilisateur[1].

### Question 8 : Compromis de conception au-delà des performances EMI

#### 3.8.1 Volume et poids

**Loi d'échelle**[1] : Inductances dominantes en volume/poids. Pour L donné, courant I :

$$
Volume \propto L \cdot I^2 \quad (énergie stockée : \frac{1}{2}LI^2)
$$

**Stratégies de réduction**[1] :
- Augmentation fréquence de coupure (⇒ L↓, mais atténuation basse fréquence↓)
- Topologie balanced : répartition L sur 2 conducteurs (L_total/2 par branche)
- Filtres multi-étages : Composants plus petits, SRF supérieure

#### 3.8.2 Coût et disponibilité

**Condensateurs Y haute tension** : Coût exponentiel avec V_rated (ex : Y2 630VAC ≈ 5× prix Y2 250VAC)[1].

**Inductances sur mesure vs COTS** : Bobinage dédié (lead time 6-12 semaines) vs catalogue (48h, mais valeurs discrètes)[1].

#### 3.8.3 Courant de fuite et sécurité

**Norme IEC 60950-1** : Limite générale 3.5 mA @ 50/60 Hz pour équipements IT raccordés secteur[3].

**Calcul**[1] :

$$
I_{leak} = 2\pi f \cdot C_{Y,total} \cdot V_{RMS} < 3.5\, mA
$$

Pour 230 VAC / 50 Hz : $\( C_{Y,total} < 48.3\, nF \)$ → contrainte forte pour filtrage CM.

#### 3.8.4 Pertes et rendement

**Pertes inductances** (échauffement)[1] :

$$
P_{DCR} = I_{RMS}^2 \cdot R_{DC}
$$

$$
P_{core} = k_e \cdot f^\alpha \cdot B^\beta \cdot V_{core} \quad (\alpha \approx 1.5, \beta \approx 2.5)
$$

**Exemple**[1] : Filtre 10 A RMS, 2× inductances 200 µH (DCR = 25 mΩ) → 5 W pertes ohmiques → ΔT ≈ 30°C (sans convection forcée).

#### 3.8.5 Tenue environnementale

**Standards aéronautiques DO-160**[23][29] :
- Températures : -55°C à +85°C (voire +125°C catégorie haute)
- Vibrations : 5-2000 Hz, 10 g RMS (MIL-STD-810)
- Altitude : Fonctionnement jusqu'à 50000 ft (pression réduite)

**Conséquences conception**[1] :
- Condensateurs : Classes H/C0G pour stabilité température
- Boîtiers : Potting pour tenue mécanique et HASS (Highly Accelerated Stress Screening)

### Question 9 : Méthodologies de test pour émissions conduites

#### 3.9.1 Configuration standard CISPR 16-2-1

**Setup de test**[5][8] :
```
[Réseau]──[LISN_L]──[Filtre EMI]──[DUT]──[Charge]
           │
      [50Ω term]──[EMI Receiver]
           
[Réseau]──[LISN_N]──[Filtre EMI]──[DUT]──[Charge]
           │
      [50Ω term]──[EMI Receiver]
```

**Éléments clés**[5][44] :
- **Plan de masse** : Tôle cuivre ≥ 2 m × 2 m, connexion basse impédance
- **Hauteur DUT** : 40 cm au-dessus plan de masse (normalisation capacités parasites)
- **Câbles** : Longueur définie (typ. 1 m), routage parallèle au plan

#### 3.9.2 Paramètres de mesure

**Bande de fréquence**[2][44] :
- CISPR 22/32 : 150 kHz – 30 MHz (équipements IT)
- MIL-STD-461 CE101 : 30 Hz – 10 kHz (très basse fréquence)
- DO-160 Section 21 : 150 kHz – 152 MHz (avionique)[35]

**Détecteurs normalisés**[5] :
- **Quasi-peak (QP)** : Charge rapide, décharge lente, simule perception auditive
- **Average (AVG)** : Valeur moyenne RMS, évite fausses alarmes sur raies étroites
- **Peak** : Valeur crête instantanée (utilisé pour pré-scan)

**Largeur de bande de résolution (RBW)**[5] :
- 200 Hz @ 150 kHz
- 9 kHz @ 150 kHz – 30 MHz (norme CISPR)

#### 3.9.3 Procédure de qualification

**Étape 1 : Pré-scan** (détecteur Peak, RBW large) → Identification fréquences critiques (< 30 min)[1].

**Étape 2 : Mesure finale** (détecteurs QP + AVG, RBW normalisée) → Conformité réglementaire (2-4 h)[1].

**Étape 3 : Séparation MD/CM** (méthodes avancées)[1] :
- **Réseaux CDN (Coupling-Decoupling Network)** : Extraction signaux différentiels
- **Sondes de courant + diviseur de puissance** : Mesure simultanée I_L et I_N, post-traitement
- **LISN asymétrique** : Mesure directe tension CM (midpoint)

### Question 10 : LISN — Rôle et fonctionnement

#### 3.10.1 Définition et objectifs

Le **Line Impedance Stabilization Network** (LISN, norme ANSI C63.4) ou **Artificial Mains Network** (AMN, norme CISPR 16-1-2) est un réseau d'impédance normalisée inséré entre le secteur et l'équipement sous test (DUT)[43][46][49].

**Trois fonctions cardinales**[43][46] :

1. **Isolation du bruit secteur** : Filtre passe-bas (inductance série 50 µH, capacité 1 µF) bloque perturbations réseau > 150 kHz
2. **Impédance normalisée** : Présente 50 Ω au DUT dans bande 150 kHz – 30 MHz (±20%, tolérance CISPR)
3. **Couplage mesure** : Dérive signal RF vers récepteur EMI sans perturber alimentation DC/AC

#### 3.10.2 Schéma de principe (V-LISN 50µH/50Ω)

```
[Secteur] ──[50µH]──[5Ω]──┬──[DUT]
                           │
                      [1µF]│[0.1µF]
                           ├─────── RF Out
                         [50Ω]    (vers EMI Rx)
                           │
                        [Masse]
```

**Impédance vue du DUT**[43][49] :

$$
Z_{LISN}(f) = \frac{50 \parallel (j2\pi f \cdot 50\mu H + 5)}{1 + j2\pi f \cdot 50 / |X_C|}
$$

- @ 150 kHz : $\( |Z| \approx 50\, \Omega \)$
- @ 30 MHz : $\( |Z| \approx 50\, \Omega \)$
- @ DC : $\( |Z| \approx 5\, \Omega \) (passage courant secteur)$

#### 3.10.3 Variantes selon application

**5 µH LISN** (automobile, DO-160)[49][52] :
- Simule impédance batteries 12/28 VDC ou alternateurs 400 Hz
- Bande mesure étendue : jusqu'à 245 MHz (CISPR 25)

**150 Ω / 1500 Ω LISN** (télécommunications)[1] :
- Lignes symétriques 600 Ω (téléphonie analogique)

#### 3.10.4 Vérification métrologique

**Tests périodiques obligatoires** (CISPR 16-1-2)[5] :
- Module d'impédance : 50 Ω ± 20% (150 kHz – 30 MHz)
- Phase d'impédance : ± 11° (équivaut à Q < 5)
- Isolation secteur : < -40 dB @ 150 kHz
- Perte d'insertion : < 0.5 dB (DC – 10 kHz)

**Équipement requis** : Analyseur de réponse en fréquence (ex: Bode 100, fixture CISPR 16-1-2 Annexe A)[1].

### Question 11 : Différence conception filtre EMI vs filtre analogique classique

#### 3.11.1 Objectifs fondamentalement distincts

**Filtre analogique** (traitement du signal)[1] :
- Objectif : Extraction/séparation bandes spectrales, distorsion minimale dans bande passante
- Critères : Gabarit fréquentiel précis (Butterworth, Chebyshev, Cauer), adaptation impédances source/charge, linéarité de phase

**Filtre EMI** (atténuation perturbations)[1][42] :
- Objectif : Réduction niveau bruit conduit/rayonné sous limites réglementaires, robustesse électrique (ESD, surtensions)
- Critères : Insertion loss élevée en bande rejet, stabilité système, contraintes normatives (courant fuite, volume, coût)

#### 3.11.2 Différences méthodologiques

**Adaptation d'impédance**[1][42] :

- **Filtre analogique** : Impédances source et charge définies et constantes (ex : 50 Ω RF, 600 Ω audio) → design pour transfert de puissance maximal $(\( |S_{11}| < -20\, dB \))$
- **Filtre EMI** : Impédances variables et inconnues sur large spectre (LISN ≠ réseau réel) → design pour **maximum de désadaptation** (réflexion perturbations vers source)[1][45]

**Fréquences de coupure**[1] :

- **Filtre analogique** : Placement précis des pôles/zéros selon gabarit (ex : Butterworth → \( Q = 0.707 \))
- **Filtre EMI** : Fréquence de coupure indicative, performance mesurée par insertion loss sur décades (slope 20/40/60 dB/décade selon ordre)[1]

**Composants**[1] :

- **Filtre analogique** : Composants faibles pertes, stabilité température (C0G, film polypropylène), coût élevé
- **Filtre EMI** : Compromis coût/volume, classes diélectriques standards (X7R acceptable), tolérance large (±20%)

#### 3.11.3 Topologies comparées

**Exemple**: Filtre passe-bas 2ème ordre, f_c = 10 kHz

**Approche analogique** (Butterworth) :

$$
L = \frac{\sqrt{2} R}{\omega_c}, \quad C = \frac{\sqrt{2}}{\omega_c R}
$$

Pour $\( R = 50\, \Omega \) : \( L = 1.125\, mH, C = 450\, nF \)$ → adaptation impédances assurée.

**Approche EMI** (même f_c, impédances réelles inconnues)[1] :

$$
L = \frac{R_d}{2\pi f_c}, \quad C = \frac{1}{2\pi f_c R_d}
$$

Pour $\( R_d = 50\, \Omega \) : \( L = 796\, \mu H, C = 318\, nF \)$ → design non adapté, maximise réflexion.

### Question 12 : Rôle de l'impédance de charge dans conception et comportement EMI

#### 3.12.1 Influence sur efficacité du filtre

**Principe de réflexion d'impédance**[42][45] : Performance optimale obtenue quand élément filtre présente impédance opposée à celle de la source/charge :

- **Impédance source basse** → Inductance série en tête de filtre (haute impédance série)
- **Impédance source haute** → Capacité shunt en tête de filtre (basse impédance parallèle)

**Quantification** (filtre π vs T, source 50 Ω, charge 1 kΩ)[42] :

| Topologie | IL @ 10 MHz | Commentaire |
|-----------|-------------|-------------|
| π (C-L-C) | 68.3 dB | Optimal (C côté charge haute-Z) |
| T (L-C-L) | 38.5 dB | Sous-optimal (L côté charge haute-Z) |
| Écart | **29.8 dB** | Facteur x30 en amplitude linéaire |

#### 3.12.2 Impédance de charge variable en fréquence

**Réalité des convertisseurs**[1] : Impédance d'entrée dépend de :
- **Basse fréquence (< 1 kHz)** : Comportement résistif négatif $(\( R_{in} = -V^2/P \))$
- **Moyenne fréquence (1 kHz – f_sw)** : Résonance filtre d'entrée convertisseur (LC + ESR)
- **Haute fréquence (> f_sw)** : Capacitance d'entrée domine $(\( Z \approx 1/j\omega C_{bulk} \))$

**Conséquence conception**[1] : Filtre multi-étages requis pour couvrir variations spectrales → caractérisation expérimentale recommandée (analyseur impédance ou méthode d'injection).

#### 3.12.3 Effet sur séparation MD/CM

**Impédance asymétrique** (câbles longueurs inégales, composants non appariés)[30] : Conversion partielle MD → CM :

$$
V_{CM,induit} \approx \frac{\Delta Z}{2Z_{moy}} \cdot V_{DM}
$$

**Exemple** : Désappariement 10% ($\( \Delta Z/Z = 0.1 \)$) sur liaison 5V DM → 250 mV CM injecté → potentiellement dépassement limite CM (ordres de grandeur différents)[30].

### Question 13 : Topologies de filtres EMI passifs de base — Description et mécanismes

#### 3.13.1 Filtre LC (L en série, C en shunt)

**Schéma** :
```
[Source] ──[L]──┬──[Charge]
                │
              [C]
                │
             [Masse]
```

**Fonction de transfert**[1] :

$$
H(s) = \frac{1}{1 + s^2LC + sRC}
$$

**Atténuation théorique** : 40 dB/décade (2 pôles) au-delà de fréquence de coupure :

$$
f_c = \frac{1}{2\pi\sqrt{LC}}
$$

**Mécanisme de suppression EMI**[42][45] :
1. **Inductance L** : Haute impédance série → bloque courants HF
2. **Capacité C** : Basse impédance shunt → détourne courants HF vers masse
3. **Fréquence de résonance** : Impédance minimale → atténuation maximale

**Application type** : Source basse impédance (< 10 Ω), charge haute impédance (> 100 Ω)[45].

#### 3.13.2 Filtre π (C-L-C)

**Schéma** :
```
      ──[C1]──┬──[L]──┬──[C2]──
              │       │
           [Masse] [Masse]
```

**Ordre** : 3 (trois éléments réactifs) → **60 dB/décade** théorique[1].

**Fonction de transfert** (simplifiée, R_S = R_L = R)[1] :

$$
H(j\omega) = \frac{1}{1 + 3(j\omega RC) + 3(j\omega RC)^2 - (j\omega)^3 R^2LC}
$$

**Avantages**[1][42] :
- Capacité d'entrée offre impédance basse dès ligne (filtrage précoce)
- Performance supérieure sur sources haute impédance (typ. 50 Ω LISN)
- Configuration la plus utilisée en pratique CEM

**Inconvénient** : Inductance centrale non chargée côté source → sensibilité résonance parasite (nécessite damping)[1].

**Valeurs composants** (conception normalisée)[1] :

$$
C_1 = C_2 = \frac{1}{4\pi f_c R_d}, \quad L = \frac{R_d}{\pi f_c}
$$

#### 3.13.3 Filtre T (L-C-L)

**Schéma** :
```
──[L1]──┬──[L2]──
        │
      [C]
        │
     [Masse]
```

**Ordre** : 3 → **60 dB/décade**[1].

**Fonction de transfert** (R_S = R_L = R)[1] :

$$
H(j\omega) = \frac{R}{R + j\omega(L_1 + L_2) + \frac{1}{j\omega C} + (j\omega)^2 L_1 L_2 C}
$$

**Avantages**[1][42] :
- Inductances d'entrée et sortie → double blocage série
- Optimal pour sources **basse impédance** (< 10 Ω, ex : lignes puissance)

**Inconvénients**[1] :
- Inductance côté charge peut "affamer" convertisseur (haute impédance @ f_sw)
- Volume/poids supérieurs (2 inductances vs 1 pour π)

**Application** : Filtres militaires haute puissance (MIL-STD-461), lignes DC batteries[1].

#### 3.13.4 Filtres multiples (double-π, double-L)

**Objectif** : Atténuations extrêmes (> 80 dB @ fréquences critiques)[1].

**Principe de cascade** : Impédances intermédiaires créent désadaptations successives → maximisation réflexions[1].

**Exemple double-π** (5 éléments)[1] :

$$
IL_{total}(f) \approx IL_{\pi1}(f) + IL_{\pi2}(f) - 6\, dB \quad (couplage résiduel)
$$

**Design pratique** : Caractéristiques impédances différentes pour chaque étage (ex : $\( Z_1 = 10\, \Omega, Z_2 = 100\, \Omega \)$) maximise effet de réflexion multi-trajet[1].

#### 3.13.5 Filtres Cauer (elliptiques)

**Spécificité** : Insertion résonateur LC série en parallèle avec inductance série → **notch** (zéro de transmission) à fréquence précise[1].

**Schéma** (filtre π avec Cauer) :
```
──[C1]──┬──[L_series]──┬──[C2]──
        │     ||       │
     [Masse] [L_notch] [Masse]
             [C_notch]
```

**Dimensionnement du notch**[1] :

$$
f_{notch} = \frac{1}{2\pi\sqrt{L_{notch} \cdot C_{notch}}}
$$

**Application** : Suppression raie harmonique dominante (ex : 3ème harmonique 150 kHz d'une alimentation 50 kHz)[1].

**Limitation** : Réduction atténuation au-delà de f_notch (impédance parallèle court-circuite inductance série) → usage combiné avec filtre large bande[1].

---

## 4. SYNTHÈSE ET CONCLUSION

### 4.1 Points clés de la conception de filtres EMI

#### 4.1.1 Approche méthodologique recommandée

**Phase 1 : Caractérisation du bruit**[1]
1. Test EMI sans filtre → scan spectral complet (Peak detector)
2. Séparation MD/CM (CDN ou sondes de courant)
3. Identification fréquences critiques et marges requises (typ. +6 à +10 dB)

**Phase 2 : Définition architecture**[1]
1. Choix topologie selon impédances source/charge (L, π, T)
2. Calcul fréquence de coupure (méthode K-factor ou pente dB/décade)
3. Dimensionnement composants (formules analytiques ou matrices ABCD)

**Phase 3 : Stabilité et optimisation**[1]
1. Vérification impédance sortie filtre < impédance entrée convertisseur
2. Ajout damping si Q > 2 (RC shunt ou RL série)
3. Simulation transitoires (step response, surtensions)

**Phase 4 : Validation expérimentale**[1]
1. Prototypage avec composants proches valeurs calculées (tolérances standards)
2. Tests EMI préliminaires (pré-compliance)
3. Ajustements itératifs (valeurs composants, damping, blindage)

#### 4.1.2 Règles de bonnes pratiques

**Sélection composants**[1] :
- Inductances : SRF > 10× f_max, saturation I_peak (non I_RMS), DCR faible
- Condensateurs X : Film pour stabilité, MLCC avec derating DC-bias vérifié
- Condensateurs Y : Respect limites IEC courant de fuite, classes sécurité appropriées

**Layout PCB/assemblage**[1] :
- Connexions basse inductance (pistes larges, vias multiples)
- Capacités traversantes (feedthrough) en sortie filtre
- Inductances en quadrature (90°) pour éviter couplage magnétique
- Blindage compartimenté (séparation filtre / convertisseur)

**Tests et validation**[1] :
- Vérification insertion loss sur impédances normalisées (50 Ω) et réelles
- Mesure impédance sortie filtre (analyseur RF ou méthode d'injection)
- Tests transitoires : réponse à échelons de charge, surtensions ligne

### 4.2 Défis actuels et perspectives

#### 4.2.1 Montée en fréquence des convertisseurs

Les convertisseurs modernes (GaN, SiC) atteignent des fréquences de commutation 1-5 MHz, voire 10 MHz en RF[1]. Conséquences :

- Bande EMI élargie (150 kHz → 100 MHz) → filtres multi-résonances
- Composants parasites critiques (traces PCB ≈ 5 nH/cm deviennent significatives)
- Couplage capacitif accentué (dV/dt > 100 V/ns) → blindage renforcé

#### 4.2.2 Miniaturisation et intégration

Contraintes avioniques/spatial exigent densités de puissance > 50 W/cm³[23] :

- Matériaux magnétiques avancés (nanocristallins, ferrites haute température)
- Filtres actifs (AEF) : Circuits d'annulation de bruit par injection de courant opposée (15-30 dB CM)[51]
- Intégration 3D : Capacités enterrées dans PCB, inductances co-packagées

#### 4.2.3 Normes et réglementation évolutives

- **CISPR 32** (2015) remplace CISPR 22 : Exigences EMC renforcées, détecteurs AVG obligatoires[2]
- **DO-160G** (2010) : Bande conduite étendue jusqu'à 152 MHz (vs 30 MHz précédemment)[35]
- **Cybersécurité** : Normes EN 18031-1 (2023) intègrent résilience EMI dans évaluation sécurité IoT[6]

---

## 5. BIBLIOGRAPHIE

### 5.1 Normes et standards

[2] CISPR 16-2, "Specification for radio disturbance and immunity measuring apparatus and methods," International Electrotechnical Commission, 2020. https://www.academyofemc.com/emc-standards (consulté le 15 décembre 2025).

[3] IEC 61000-6-1, "Electromagnetic compatibility (EMC) – Part 6-1: Generic standards – Immunity for residential, commercial and light-industrial environments," 2022. https://www.dlsemc.com/iec-en-61000-6-1 (consulté le 15 décembre 2025).

[4] MIL-STD-461G, "Requirements for the control of electromagnetic interference characteristics of subsystems and equipment," U.S. Department of Defense, 2015. https://intrinsicallysafestore.com/blog/mil-std-461-compliance (consulté le 15 décembre 2025).

[5] CISPR 16-1-2, "Specification for radio disturbance and immunity measuring apparatus and methods – Part 1-2: Radio disturbance and immunity measuring apparatus – Ancillary equipment – Conducted disturbances," IEC, 2014. https://www.tekbox.com/product/Pre-Compliance_Conducted_Emission_Measurements.pdf (consulté le 15 décembre 2025).

[9] IEC 61000 (famille), "Electromagnetic compatibility (EMC)," https://en.wikipedia.org/wiki/List_of_common_EMC_test_standards (consulté le 15 décembre 2025).

[22] FCC Part 15, "Radio frequency devices," U.S. Code of Federal Regulations, Title 47. https://www.testups.com/fcc-part-15-requirements/ (consulté le 15 décembre 2025).

[23] RTCA DO-160G, "Environmental conditions and test procedures for airborne equipment," Radio Technical Commission for Aeronautics, 2010. https://atslab.com/standard/rtca-do-160-emi-testing/ (consulté le 15 décembre 2025).

### 5.2 Ouvrages techniques

[1] R. L. Ozenbaugh et T. M. Pullen, *EMI Filter Design, Third Edition*, CRC Press, 2012 (Fichier PDF fourni : MEE7-EMI-Filter-Design.pdf).

[8] CISPR Technical Report 16-2-5, "In situ electromagnetic disturbance measurements," 2008. https://cdn.standards.iteh.ai/samples/13617/dd55a5d78e644b72bf7b8c24c3672144/CISPR-TR-16-2-5-2008.pdf (consulté le 15 décembre 2025).

### 5.3 Webinaires et présentations techniques

[1] (vidéo) Flex Power Modules, "EMI filter design [Technical Webinar]," 1er octobre 2025, https://www.youtube.com/watch?v=w_UBNx12_n4 (consulté le 16 décembre 2025). Transcript intégral analysé.

### 5.4 Articles scientifiques et notes d'application

[24] P. Musznicki et al., "Detailed analysis of common mode and differential mode conducted emission in buck converter," *Poznan University of Technology*, 2016. https://archiwum.pe.org.pl/articles/2016/8/60.pdf (consulté le 15 décembre 2025).

[27] Vittorio Ferrari (University of Brescia), "Understanding Common Mode Noise," Note technique ES2M. https://vittorio-ferrari.unibs.it/ES2M/Understanding%20Common%20Mode%20Noise.pdf (consulté le 15 décembre 2025).

[30] Altium, "A Guide to Mode Conversion, Its Causes, and Solutions," 2025. https://resources.altium.com/p/guide-mode-conversion-its-causes-and-solutions (consulté le 15 décembre 2025).

[42] In Compliance Magazine, "EMC Filters Comparison Part II: π and T Filters," K. Wyatt, avril 2024. https://incompliancemag.com/emc-filters-comparison-part-ii-π-and-t-filters/ (consulté le 15 décembre 2025).

[47] Texas Instruments, "A review of EMI standards, part 1 – conducted emissions," Application Report SSZT673, 2024. https://www.ti.com/lit/pdf/sszt673 (consulté le 15 décembre 2025).

### 5.5 Ressources industrielles et guides pratiques

[7] Relec Electronics, "Defence EMI Filter Modules for MIL-STD-461 Compliance," 2025. https://www.relec.co.uk/defence-emi-filter-modules-for-mil-std-461-compliance/ (consulté le 15 décembre 2025).

[43] Teseq (LISN documentation), "LISN / Artificial Mains Network specifications," https://www.tssj.co.jp/analyzer_emc/pdf/LISN.pdf (consulté le 15 décembre 2025).

[44] EMC Fastpass, "Radiated & Conducted Emissions Testing – Beginner's Guide," 2025. https://emcfastpass.com/emc-testing-beginners-guide/emissions/ (consulté le 15 décembre 2025).

[45] Interference Technology, "Selecting the Proper EMI Filter Circuit For Military and Defense Applications," K. Hill, novembre 2017. https://interferencetechnology.com/selecting-proper-emi-filter-circuit-military-defense-applications/ (consulté le 15 décembre 2025).

[49] Schwarzbeck Mess-Elektronik, "LISN Line Impedance Stabilisation Networks / AMN Artificial Mains Network," https://www.schwarzbeck.de/en/lisn-line-impedance-stabilisation-networks.html (consulté le 15 décembre 2025).

[51] IQS Directory, "Applications and Benefits of EMI Filters," https://www.iqsdirectory.com/articles/power-supply/emi-filters.html (consulté le 15 décembre 2025).

### 5.6 Bases de données normatives

[6] EN IEC 61000-6-3, "Generic emission standard for residential, commercial and light-industrial environments," https://www.dlsemc.com/iec-en-61000-6-3 (consulté le 15 décembre 2025).

[11] CISPR 22, "Information technology equipment – Radio disturbance characteristics – Limits and methods of measurement," (remplacé par CISPR 32 en 2015). https://plcdocsearch.uma.es/Proceedings/2002/pdf/09110115.pdf (consulté le 15 décembre 2025).

---

## 6. ANNEXES

### Annexe A : Tableaux de composants typiques

**Tableau A.1 : Inductances de mode commun (sélection commerciale)**

| Référence | L_CM (mH) | I_rated (A) | DCR (mΩ) | L_leak (µH) | Matériau | Fabricant |
|-----------|-----------|-------------|----------|-------------|----------|-----------|
| WE-CMB 744823 | 10 | 3 | 120 | 15 | Ferrite MnZn | Würth |
| Coilcraft B82726 | 2.2 | 10 | 18 | 3.5 | Nanocrystallin | Coilcraft |
| Murata DLW5BTM | 0.47 | 5 | 45 | 0.8 | Ferrite NiZn | Murata |

**Tableau A.2 : Condensateurs pour filtres CEM**

| Type | Tension | Capacité | ESR @ 100kHz | SRF | Application |
|------|---------|----------|--------------|-----|-------------|
| MLCC X7R 1210 | 100V | 4.7µF | 8 mΩ | 4 MHz | X-cap (derating requis) |
| Film PP MKP | 275VAC | 1µF | 15 mΩ | 12 MHz | X-cap (stable) |
| Céramique Y2 | 300VAC | 4.7nF | 50 mΩ | 25 MHz | Y-cap (sécurité) |
| Feedthrough | 250VAC | 10nF | 20 mΩ | 100 MHz | Y-cap traversant |

### Annexe B : Check-list de design de filtre EMI

**Phase de spécification** :
- [ ] Norme applicable identifiée (CISPR, MIL-STD, DO-160, FCC)
- [ ] Limites conduites/rayonnées répertoriées (dBµV, dBµA)
- [ ] Puissance, tension, courant équipement définis
- [ ] Fréquence de commutation et harmoniques calculés
- [ ] Contraintes volume/poids/coût fixées

**Caractérisation pré-design** :
- [ ] Scan EMI sans filtre réalisé (Peak detector, 9 kHz – 30 MHz)
- [ ] Fréquences critiques identifiées (marges > 6 dB)
- [ ] Séparation MD/CM effectuée (CDN ou sondes)
- [ ] Impédance d'entrée convertisseur mesurée ou calculée

**Design et simulation** :
- [ ] Topologie choisie (L, π, T) selon impédances source/charge
- [ ] Fréquence de coupure calculée (méthode K-factor)
- [ ] Composants dimensionnés (L, C, damping)
- [ ] Simulation SPICE avec parasites (ESR, ESL, SRF)
- [ ] Vérification stabilité (Z_out < R_in_converter)

**Prototypage et validation** :
- [ ] Layout PCB optimisé (quadrature inductances, vias multiples)
- [ ] Composants COTS ou prototypes inductances
- [ ] Tests insertion loss (50 Ω + impédances réelles)
- [ ] Tests transitoires (échelons charge, surtensions)
- [ ] Qualification EMC complète (labo accrédité)

### Annexe C : Exemples de setups de test

**Setup 1 : Émissions conduites CISPR 16-2-1**

```
Enceinte blindée (< -80 dB @ 30 MHz)
┌─────────────────────────────────────────────┐
│  [Plan de masse 2m × 2m]                    │
│                                              │
│   [LISN] ───40cm───> [DUT]                  │
│     │                  │                     │
│   [50Ω] ──RF──> [EMI Rx]  ──> [Charge]     │
│                                              │
│   Câbles : longueur 1m, hauteur 5cm         │
│   RBW : 9 kHz, détecteurs QP+AVG           │
└─────────────────────────────────────────────┘
```

**Setup 2 : Séparation MD/CM par sondes de courant**

```
[LISN_L] ──[Sonde I_L]──> [Filtre EMI] ──> [DUT]
              │
         [Splitter] ──> [Port 1] : (I_L + I_N)/2 = I_CM
              │
[LISN_N] ──[Sonde I_N]──> [Filtre EMI] ──> [DUT]
                     │
                 [Port 2] : (I_L - I_N)/2 = I_DM
```

**Setup 3 : Mesure impédance sortie filtre (méthode d'injection)**

```
[Signal Gen] ──[Transformateur d'injection]──> [Point mesure]
                                                      │
                                              [Filtre EMI + DUT]
                                                      │
[Analyseur FFT] <──[Sonde tension]────────────────────┘
                <──[Sonde courant]

Z_out(f) = V_mesure(f) / I_mesure(f)
```

---




