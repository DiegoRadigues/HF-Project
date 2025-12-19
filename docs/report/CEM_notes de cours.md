# Compatibilité Électromagnétique (EMC/CEM)

## Table des matières

1. Introduction à la CEM
2. Principes fondamentaux et définitions
3. Chemins de couplage des perturbations
4. Couplage par impédance commune
5. Couplage inductif
6. Modes de propagation des perturbations
7. Solutions et bonnes pratiques

---



### 1.3 Exemples d'incompatibilités

Plusieurs incidents historiques et récents illustrent l'importance de la CEM :

- **HMS Sheffield (1982)** et **USS Forrestal (1967)** : Défaillances systèmes critiques
- **Aéroports** : Les autoroutes à proximité d'aéroports doivent être blindées
- **Automobiles** : Véhicules devenant « fous » en proximité d'aéroports
- **Téléphones mobiles** : Activation accidentelle d'équipements (toits ouvrants, serrures centralisées)
- **Appareils électroniques** : Pertes d'synchronisation, arrêts inopinés

### 1.4 Sources de perturbations électromagnétiques (EMI)

Les sources de perturbations peuvent être naturelles ou d'origine humaine :

- **Sources basse fréquence** : Réseaux de distribution électrique (50-60 Hz)
- **Sources haute fréquence** : Antennes, micro-ondes, appareils numériques
- **Sources naturelles** : Aurores boréales, vent solaire, rayons cosmiques
- **Sources de l'environnement** : Moteurs AC/DC, onduleurs, électronique de puissance
- **Électricité statique** : Décharges électrostatiques
- **Phénomènes électrochimiques** : Thermocouples
- **Foudre** : Impulsions massives

---

## 2. Principes Fondamentaux et Réglementation

### 2.1 Critères de performance

La norme CEM définit quatre critères de performance :

**Critère A** : Performance normale dans les limites spécifiées par le fabricant

**Critère B** : Perte temporaire de fonction qui cesse avec la perturbation et dont l'équipement se rétablit sans intervention de l'opérateur

**Critère C** : Perte temporaire de fonction nécessitant l'intervention de l'opérateur pour correction

**Critère D** : Perte permanente de fonction avec dommage matériel, logiciel ou perte de données

### 2.2 Réglementation européenne

**Directif EMC 2014/30/UE** (révision de 89/336/CEE de 1989) :

- **Obligatoire depuis 1996** pour commercialisation en Union Européenne
- **Marquage CE** requis pour certains équipements
- Exige que :
  1. Les perturbations EM générées soient limitées à un niveau permettant aux autres appareils de fonctionner
  2. Les appareils aient une immunité suffisante contre les perturbations EM

### 2.3 Normes de référence (CEI 1000)

**CEI 1000-1** : Généralités, définitions, principes

**CEI 1000-2** : Environnement, classification

**CEI 1000-3** : Limites d'émission et d'immunité

**CEI 1000-4** : Techniques d'essais et de mesures

**CEI 1000-5** : Guides d'installation et d'atténuation

### 2.4 Normes génériques

- **EN 61000-6-1** : Immunité environnement résidentiel
- **EN 61000-6-2** : Immunité environnement industriel
- **EN 61000-6-3** : Émission environnement résidentiel
- **EN 61000-6-4** : Émission environnement industriel

### 2.5 Marque CE et directives connexes

Le marquage CE ne couvre **PAS uniquement** la CEM, mais aussi :

- **Directive Machines (2006/42/CE)** : Sécurité des personnes
- **Directive Basse Tension (2014/35/UE)** : Sécurité électrique
- **Directive Jouets (2009/48/CE)**
- **Directive Éco-conception (2009/125/CE)**

---

## 3. Équations de Maxwell et Domaines Fréquentiels

### 3.1 Équations de Maxwell

Ces équations fondamentales décrivent le comportement des champs électromagnétiques :

**Domaine temporel** :

- $\nabla \cdot E = \frac{\rho}{\varepsilon_0}$ (Gauss)
- $\nabla \cdot B = 0$ (Gauss pour magnétisme)
- $\nabla \times E = -\frac{\partial B}{\partial t}$ (Faraday)
- $\nabla \times B = \mu_0 J + \mu_0 \varepsilon_0 \frac{\partial E}{\partial t}$ (Ampère)

**Domaine fréquentiel** :

- $\nabla \cdot E = \frac{\rho}{\varepsilon_0}$
- $\nabla \cdot \mu H = 0$
- $\nabla \times E = -j \omega \mu H$
- $\nabla \times H = J - j \omega \varepsilon E$

### 3.2 Conversion temps-fréquence

Les signaux non-sinusoïdaux contiennent des harmoniques (séries et transformées de Fourier).

**Importance pour l'EMC** : Les problèmes EMI/EMC sont majoritairement liés au contenu haute fréquence des signaux.

---

## 4. Bande Passante des Signaux Numériques

### 4.1 Onde carrée et harmoniques

Une onde carrée idéale a un spectre d'enveloppe en **-20 dB/décade** avec amplitude décroissante en 1/n pour l'harmonique n.

**Reconstruction progressive** :
- H1-H3-H5 : Forme grossière
- H1-...H11 : Définition meilleure
- H1-...H19 : Ressemblance à onde carrée

### 4.2 Contenu spectral et fronts de montée

**Plus le contenu en hautes harmoniques est élevé, plus les fronts de montée sont raides.**

Pour une onde trapézoïdale réaliste :
- **tr** = temps de montée (10% à 90%)
- **tf** = temps de descente (10% à 90%)
- **τ** = largeur d'impulsion

### 4.3 Modèle circuit RC et bande passante

**Hypothèse** : Le front de montée se comporte comme un circuit RC sans ondulation.

$$v(t) = A(1 - e^{-t/\tau})$$

avec $\tau = RC$

**Fréquence de coupure** : $f_c = \frac{1}{2\pi RC}$

**Relation temps-domaine/fréquence** :

$$RC = \tau = \frac{t_r}{2,2}$$

$$f_c = \frac{2,2}{2\pi t_r} = \frac{0,35}{t_r}$$

**Bande passante du signal numérique** :

$$\boxed{BW = \frac{0,35}{t_r}}$$

(où $t_r$ est le temps de montée le plus court, entre montée et descente)

### 4.4 Bande passante à -3dB

La bande passante à -3dB représente la fréquence où la puissance est tombée à 50% (ou l'amplitude à 70%) de la puissance d'une onde carrée idéale de même amplitude et rapport cyclique.

---

## 5. Chemins de Couplage (Coupling Paths)

### 5.1 Vue générale

**Trois éléments essentiels** sont nécessaires pour qu'une perturbation se produise :

1. **Source EMI** : Dispositif générant la perturbation
2. **Victime** : Dispositif affecté par la perturbation
3. **Chemin de couplage** : Lien de transmission entre source et victime

### 5.2 Types de couplage

**1. Couplage par impédance commune** (Conducted coupling)
- Effet d'un courant de perturbation traversant un conducteur victime
- L'impédance d'un conducteur n'est jamais zéro
- Mode de couplage **uniquement conductif**

**2. Couplage inductif** (Inductive diaphony / Mutual inductance)
- Effet du courant variable sur une boucle de circuit étroitement couplée
- Courant variable crée champ magnétique variable B(t)
- Flux magnétique induit tension : $V = \frac{d\Phi}{dt}$

**3. Couplage capacitif** (Capacitive diaphony)
- Effet d'une tension variable entre 2 conducteurs proches
- La parasitaire capacitance entre conducteurs n'est jamais zéro
- Crée courant parasite par variation de tension

**4. Couplage champ-conducteur** (Field-to-wire coupling)
- Effet d'un champ électrique variable sur un conducteur
- Tout conducteur droit peut agir comme antenne
- Effet antenne : champ électrique induit courant

**5. Couplage champ-boucle** (Field-to-loop coupling)
- Effet d'un champ magnétique variable sur une boucle
- Tout circuit fermé peut agir comme antenne
- Loi de Lenz-Faraday : $e = \frac{d\Phi}{dt}$

### 5.3 Combinaisons de couplage typiques

- Champ vers fil → courant
- Impédance commune → tension
- Circuit-masse → couplage composé

---

## 6. Couplage par Impédance Commune

### 6.1 Principe et modèle

L'**impédance commune** est l'effet d'un courant de perturbation s'écoulant dans un conducteur victime.

C'est le **seul mode de couplage purement conductif**.

**Circuit typique** : VHS magnétoscope avec interférence entre signal audio analogique et signal vidéo numérique partageant le chemin de retour.

### 6.2 Modèle du conducteur : Résistance et Inductance

Tout conducteur électrique possède deux paramètres critiques :

**Résistance série (R)** :
- Dépend de la résistivité du matériau
- Dépend des dimensions
- Formule de Pouillet : $R = \rho \frac{l}{S}$

| Paramètre | Valeur |
|-----------|--------|
| $\rho$ : résistivité (Ω⋅m) | Material property |
| $l$ : longueur conducteur (m) | Geometric |
| $S$ : section conducteur (m²) | Geometric |

**Résistivité à 25°C** :
- **Cuivre** : $\rho = 17 \times 10^{-9}$ Ω⋅m
- **Aluminium** : $\rho = 26 \times 10^{-9}$ Ω⋅m
- **Acier carbone** : $\rho = 143 \times 10^{-9}$ Ω⋅m

**Inductance série (L)** :
- Dépend des dimensions du conducteur
- Dépend de la forme du conducteur
- Dépend du mode de propagation
- Dépend de la perméabilité magnétique du matériau

**Note** : La capacitance du conducteur n'est pas un problème d'impédance commune (voir couplage capacitif).

### 6.3 Modèle à basse fréquence : Résistance seule

À basse fréquence, l'impédance est déterminée principalement par la **résistance**.

**PCB (circuit imprimé) standard** :
- Piste cuivre 35 µm (1 oz)
- $R = 0,486 \frac{L}{W} \approx 0,5 \frac{L}{W}$ [mΩ]
  - $L$ : longueur de piste
  - $W$ : largeur de piste
  
Avec $L$ et $W$ dans les mêmes unités, $R$ en mΩ.

### 6.4 Effet de peau (Skin Effect)

À haute fréquence, le courant ne circule que dans une couche superficielle du conducteur.

**Profondeur de peau** :

$$\delta = \frac{1}{\sqrt{\pi f \mu_0 \mu_r \sigma_0 \sigma_r}} \approx \frac{66}{\sqrt{f_{MHz} \mu_r \sigma_r}} \text{ [µm]}$$

Où :
- $\delta$ : profondeur de peau (µm)
- $f_{MHz}$ : fréquence (MHz)
- $\mu_r$ : perméabilité relative (Air = 1, Fer = 100+)
- $\sigma_r$ : conductivité relative (Cu = 1)

**Exemples pour le cuivre** :
- **50 Hz** : $\delta = 9,38$ mm
- **1 MHz** : $\delta = 70$ µm
- **100 MHz** : $\delta = 7$ µm

### 6.5 Solutions à l'effet de peau

**Conducteurs creux** : Pour puissance élevée, basse fréquence

**Fil de Litz** : Câble spécialisé où chaque fil est isolé individuellement, réduisant les pertes par effet de peau à puissance intermédiaire et haute fréquence

### 6.6 Impédance de surface

Pour un conducteur en feuille (plan de masse, piste PCB, boîtier métallique) :

**Résistance de surface** (Ω/carré) :

$$R_{\square} = \frac{\rho}{e}$$

Où $e$ est l'épaisseur du conducteur.

**DC** : $R_{\square} = \frac{\rho_{(µ\Omega m)}}{e_{(mm)}}$

**Comportement HF** :

Si épaisseur $e < 0,7\delta$ : Conducteur se comporte comme résistance constante

Si épaisseur $e > 0,7\delta$ : Impédance augmente avec $\sqrt{f}$

**Fréquence de transition** $f$ pour $e = 0,7\delta$ :

$$Z_{\square} = 370 f_{MHz} \sqrt{\frac{\mu_r}{\sigma_r}} \text{ [µΩ]}$$

**Impédance de surface relative** (par rapport au cuivre) :
- Argent : 0,97
- Aluminium : 1,26
- Fer/acier : 7,5-10 (très élevé !)

### 6.7 Inductance linéique du conducteur

Tout conducteur stocke de l'énergie dans le champ EM : $W = \frac{1}{2}LI^2$

**Très basse fréquence** :
- Inductance linéique : $L_{lin} = 0,05$ µH/m
- Dépend uniquement de la longueur
- Généralement négligeable sauf très grandes longueurs

**Haute fréquence** :
- Inductance non négligeable : $jL$
- Impédance totale : $Z = R + jL$
- Phase : rarement comparable (R et L d'ordres différents)

**Facteur de qualité** : $Q = \frac{L}{R}$
- Inductance bobinée : $Q < 200$
- Inductance involontaire : $Q < 20$
- Matériaux ferromagnétiques : $L$ diminue, saturation possible

### 6.8 Inductance linéique : Mode commun vs Mode différentiel

**Mode commun (MC)** :
- Courant revient par les masses
- Champ magnétique : $H \propto 1/r$
- Énergie stockée dans l'air
- $L_{lin} \approx 1$ µH/m

**Mode différentiel (MD)** :
- Courant revient par fil de retour proche
- Champ magnétique : $H \propto 1/r^2$
- Énergie stockée dans l'isolant
- $L_{lin} = 0,35$ µH/m (fil seul)
- $L_{lin} = 0,70$ µH/m (paire aller+retour)

### 6.9 Formules d'inductance

**Inductance d'un conducteur droit** (basse fréquence) :

$$L = 0.002 \cdot l \cdot (\ln(4l/d) - 0.75) \text{ [µH]}$$

Où $l$ et $d$ sont en cm.

### 6.10 Impédance linéique et effets géométriques

À 3 kHz avec section 1 mm² :
- Effet inductif > Effet résistif

À 50 Hz avec section > 50 mm² :
- Résistance diminue si section augmente
- **Mais** tension entre les 2 bornes du câble n'augmente pas (car $L > R$)
- Solution : Augmenter équipotentialité par maillage

**Effet de température** :
- Résistance augmente avec température (~2% par 5°C)
- Pas d'effet sur inductance

**Effets géométriques** :
- Mode cheveux épingle : $L/2$
- Paire torsadée : $L/3$ à $L/5$
- PCB : 10 nH/cm typique
- Haute fréquence : 1 nH/mm (exemple : 0,6 nH/mm entre pattes de condensateur)

### 6.11 Modèle haute fréquence des condensateurs

Les condensateurs réels ne sont pas idéaux à haute fréquence.

**Composants du modèle HF** :
- $C$ : Capacitance nominale
- $ESR$ : Résistance série équivalente
- $ESL$ : Inductance série équivalente

**L'ESL limite l'efficacité à haute fréquence** et peut créer des oscillations LC.

### 6.12 Équipotentialité et longueur de conducteur

La longueur maximale d'un conducteur pour assurer l'équipotentialité dépend de la fréquence.

**Impédance caractéristique typique** :
- IC classique : 100 Ω
- Câble coaxial : 50-75 Ω
- Paire différentielle : 120 Ω

**Le conducteur doit avoir une impédance basse relative à ces valeurs.**

**Règle pratique** :
$$\text{Tous les conducteurs doivent être } < \frac{1}{30}\lambda$$

Au-delà de 1/30 de $\lambda$, le conducteur devient une antenne efficace et n'assure plus l'équipotentialité.

---

## 7. Couplage Inductif

### 7.1 Principe de la diaphonie

Le couplage inductif est un **couplage champ proche magnétique** basé sur :

1. Courant variable $i_{EMI}(t)$ crée un champ magnétique variable $B_{EMI}(t)$ et $H_{EMI}(t)$
2. Le champ variable $B_{EMI}(t)$ crée flux magnétique variable $\Phi_{EMI}(t)$ à travers surface $S$ du circuit récepteur
3. Le flux variable $\Phi_{EMI}(t)$ crée tension induite $V_{EMI}(t)$ selon loi Lenz-Faraday : $V_{EMI} = \frac{d\Phi}{dt}$

### 7.2 Modèle d'inductance mutuelle

Le couplage entre 2 circuits peut être modélisé comme une **mutuelle inductance M** (Henry).

**Équation temporelle** :

$$V_{EMI,pp} = M \frac{\Delta I_{EMI}}{\Delta T}$$

Où :
- $V_{EMI,pp}$ : tension induite crête-à-crête [V]
- $M$ : mutuelle inductance [H]
- $\Delta I_{EMI}$ : variation de courant [A]
- $\Delta T$ : temps de montée 10%-90% $t_r$ [s]

**Équation fréquentielle** :

$$V_{EMI} = j\omega M I_{EMI}$$

Où :
- $V_{EMI}$ : amplitude tension induite [V]
- $I_{EMI}$ : amplitude courant EMI [A]

La tension induite dépend aussi des **impédances du circuit récepteur** !

### 7.3 Diaphonie (Crosstalk)

**Diaphonie capacitive ou inductive** : Pas de diaphonie en DC, négligeable sous quelques kHz.

**Exemple d'équivalence de perturbation** :
- 1000 A à 50 Hz
- 1 A à 50 kHz
- 1 mA à 50 MHz

Tous donnent approximativement le **même niveau EMI**.

**Source principale** : Harmoniques des courants en mode commutation (électronique de puissance).

### 7.4 Mode différentiel à basse fréquence

**Caractéristiques** :
- Tension EMI induite entre conducteur source et conducteur victime
- Petite distance entre les 2 conducteurs
- Petite surface de boucle
- Tension induite faible
- Dépend de la géométrie (forme, taille) du circuit

### 7.5 Mode différentiel à haute fréquence

**Pire cas** : Longueur commune > λ/2 de la source EMI

**Diaphonie définie comme ratio** :
- Tension victime = pourcentage de tension source EMI
- Courant victime = pourcentage de courant source EMI

**Caractéristiques** :
- Indépendant de la fréquence
- Indépendant de la longueur commune
- Dépend uniquement de la géométrie des circuits

$D_{max}$ : Diaphonie pire cas (peut atteindre **80%** !)

### 7.6 Mode différentiel : Réduction de diaphonie

**Deux cas** selon relation entre temps de montée et temps propagation :

**Cas 1** : Temps de montée $t_r < 2T$ (montée rapide)
- Diaphonie maximale : $D = D_{max}$

**Cas 2** : Temps de montée $t_r > 2T$ (montée lente)
- Facteur de correction : $D = D_{max} \cdot \frac{2T}{t_r}$

Où $2T$ est le temps aller-retour du signal induit.

**Vitesse de propagation** : 11 ns/m pour paire de conducteurs (mode différentiel)

### 7.7 Mode commun

**Caractéristiques** :
- Tension induite entre conducteur fautif et conducteur victime le plus proche de la terre
- Meilleur cas : conducteur victime proche de conducteur terre
- Dépend de la géométrie
- $D_{max}$ peut atteindre **80%** !
- **Diaphonie commun mode toujours plus élevée que mode différentiel**

**Vitesse de propagation** : 7 ns/m par mètre longueur commune (mode commun)

### 7.8 Modèle de diaphonie maximale

**Paramètres** :
- $d$ : diamètre conducteur
- $e$ : espacement entre conducteurs
- $h$ : hauteur au-dessus du plan de référence

### 7.9 Pire cas : Câble PATA 40 conducteurs

Le câble PATA 40 conducteurs sans blindage : $D_{max} = 80\%$ !

### 7.10 Solutions : Réduction de diaphonie

**Mode différentiel (Câblage/Routage)** :
- Augmenter distance entre conducteurs « sales » et « sensibles » (10 cm avec proximité plan référence, 30 cm sinon)
- Torsade de paires avec pas différent
- Câbles blindés
- Paires UTP, STP, câble téléphone

**Mode différentiel (PCB)** :
- Réduction mutuelle inductance
- Distance minimale : 1 cm (avec plan de masse, diaphonie négligeable)
- Conducteur aller et retour proches
- Anneau de garde
- Paires différentielles
- Croisement de pistes à 90°

**Mode commun (Solutions communes)** :
- Augmenter distance (10 cm - 30 cm)
- Terre correcte (voir couplage impédance commune)
- Filtrage
- Blindage magnétique

---

## 8. Modes de Propagation des Perturbations

### 8.1 Mode différentiel (MD)

**Mode normal de transmission de signal**.

\begin{figure}
\centering
\includegraphics[width=0.6\textwidth]{differential-mode.png}
\caption{Mode différentiel : courant aller-retour normal}
\label{fig:dm}
\end{figure}

**Caractéristiques** :
- Courant aller et retour équilibrés
- Généralement pas majeur problème EMC
- Impédance charge : $Z_L$, $Z_S$ (source)
- Tension différentielle : $V_{MD}$

### 8.2 EMI mode différentiel

L'EMI peut être transmis :
1. Comme signal normal (courant/tension équilibrés)
2. Superposé sur un signal (perturbation HF sur signal utile)
3. Comme composante HF d'un signal

### 8.3 Mode commun (MC)

**Principal problème EMC, majoritairement problème haute fréquence**.

**Caractéristiques** :
- Courant aller et retour **non équilibrés**
- Les deux conducteurs portent le même courant vers la masse
- Couplage boucle-câble

### 8.4 Modelé EMI mode commun

Le mode commun représente une source de courant supplémentaire en mode commun $(I_{MC}/2)$ sur chaque ligne.

---

## 9. Résumé des Solutions EMC


### 9.2 Stratégies de réduction

**1. Réduire les émissions de la source**
- Ralentir les temps de montée/descente
- Filtrer les hautes fréquences
- Blindage
- Éloigner la source

**2. Réduire l'efficacité du chemin de couplage**
- Augmenter distance
- Torsader les paires
- Utiliser des paires blindées
- Plan de masse continu en PCB
- Croisement pistes perpendiculaire

**3. Augmenter l'immunité de la victime**
- Filtrage à l'entrée
- Blindage de l'équipement
- Terre correcte
- Séparation des circuits

---
