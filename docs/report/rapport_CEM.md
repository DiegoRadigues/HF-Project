# Rapport CEM
### Diego de Radiguès 20342

## 1. Risques potentiels identifiés

### 1.1. Zone RF autour du module RFM95W et de l'antenne

-   Le module LoRa (RFM95W) possède des pistes assez longues avant d'atteindre la zone d'antenne.
-   Risque : lignes de transmission non contrôlées pertes, réflexions, rayonnements.
-   Virages à angles droits sur la piste RF → discontinuités d'impédance.
-   Via inductance : ~ 0,6–1 nH par via typique 1,6 mm  à 868 MHz, non négligeable vs 50 Ω → dé-accord possible et Q abaissé (et donc rendement). [IPC-1999 – Design Guide for High-Speed Controlled Impedance Circuit Boards](https://www.polarinstruments.com/support/cits/IPC1999.pdf)

  ### 1.2. Routage USB non différentiel

-   Les lignes USB ne pas routées en paire différentielle avec impédance contrôlée et forment une boucle.
-   Risque : dégradation du signal + EMI.

<p align="center">
  <img width="1864" height="858" alt="boucle1" src="https://github.com/user-attachments/assets/ac47d406-4836-42a3-b020-26b665e3f2ad" />
</p>



### 1.3 Boucle sur l'alimentation du M8Q
- Sensibilité importante aux interférences au vu de surface importante qui capte une grande quantité de flux

<p align="center">
  <img width="578" height="595" alt="boucle2" src="https://github.com/user-attachments/assets/dbfe5758-f108-427c-bac6-01d0305aa59b" />
</p>



### 1.4. Absence de plan de masse continu autour du MCU

-   Risque : augmentation du bruit EMI et perturbations.
-   Le SAM-M8Q est placé environ au milieu-gauche. La doc u-blox recommande une grande masse homogène (≈ 50×50 mm) sous la patch, sans ruptures, avec un keep-out métallique autour. [Datasheet SAM-M8Q](../../docs/datasheet/SAM-M8Q.pdf)


### 1.5 Longueur des pistes trop importante entre BMS et C12 C13 C14
<p align="center">
  <img width="270" height="281" alt="C12C13C14" src="https://github.com/user-attachments/assets/939822b5-1cf9-410f-922c-8d5d062cbc5e" />
</p>



------------------------------------------------------------------------

## 2. Points positifs

### 2.1. Bonne zone KEEP OUT RF

-   bon respect de l'isolation autour de l'antenne de l'ESP.

### 2.2. Séparation fonctionnelle correcte

-   Zones RF, MCU, alimentation structurées.

