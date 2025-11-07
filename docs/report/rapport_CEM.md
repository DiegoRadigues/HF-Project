# Rapport CEM
### Diego de Radiguès 20342

## 1. Risques potentiels identifiés

### 1.1. Zone RF autour du module RFM95W et de l'antenne

-   Le module LoRa (RFM95W) possède des pistes assez longues avant d'atteindre la zone d'antenne.
-   Risque : lignes de transmission non contrôlées pertes, réflexions, rayonnements.
-   Virages à angles droits sur la piste RF → discontinuités d'impédance.

### 1.2. Absence de plan de masse continu autour du MCU

-   Risque : augmentation du bruit EMI et perturbations.

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

-   Zones RF, MCU, alimentation, SWD structurées.

### 2.3. Alimentation compacte

-   Limite les boucles bruyantes.

### 2.4. Résistances série sur signaux sensibles

-   Bon amortissement EMI.

