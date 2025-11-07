# Rapport CEM
### Diego de Radiguès 20342

## 1. Risques potentiels identifiés

### 1.1. Zone RF autour du module RFM95W et de l'antenne

-   Le module LoRa (RFM95W) possède des pistes assez longues avant d'atteindre la zone d'antenne.
-   Risque : lignes de transmission non contrôlées pertes, réflexions, rayonnements.
-   Virages à angles droits sur la piste RF → discontinuités d'impédance.
-   Via inductance : ~ 0,6–1 nH par via typique 1,6 mm  à 868 MHz, non négligeable vs 50 Ω → dé-accord possible et Q abaissé (et donc rendement). [IPC-1999 – Design Guide for High-Speed Controlled Impedance Circuit Boards](https://www.polarinstruments.com/support/cits/IPC1999.pdf)


### 1.2. Absence de plan de masse continu autour du MCU

-   Risque : augmentation du bruit EMI et perturbations.
-   Le SAM-M8Q est placé environ au milieu-gauche. La doc u-blox recommande une grande masse homogène (≈ 50×50 mm) sous la patch, sans ruptures, avec un keep-out métallique autour. [Datasheet SAM-M8Q](../../docs/datasheet/SAM-M8Q.pdf)


### 1.3. Routage USB non différentiel

-   Les lignes USB ne pas routées en paire différentielle avec impédance contrôlée.
-   Risque : dégradation du signal + EMI.

### 1.4. Longues pistes parallèles

-   Risque de diaphonie entre signaux numériques rapides.

### 1.5. Connecteur SWD non isolé

-   Peut rayonner ou être perturbé par d'autres signaux.

### 1.6. Boucles de courant larges

-   Les grandes boucles peuvent agir comme antennes → émissions EMI.

------------------------------------------------------------------------

## 2. Points positifs

### 2.1. Bonne zone KEEP OUT RF

-   bon respect de l'isolation autour de l'antenne de l'esp.

### 2.2. Séparation fonctionnelle correcte

-   Zones RF, MCU, alimentation structurées.

### 2.3. Alimentation compacte

-   Limite les boucles bruyantes.

### 2.4. Résistances série sur signaux sensibles

-   Bon amortissement EMI.

