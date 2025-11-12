# Rapport de laboratoire : Analyseur de spectre (1)  
## Résultats et discussion  

### 1. Signal sinusoïdal – 1 MHz  
**Image 1 :**  
On observe un **seul pic centré à 1 MHz** avec une amplitude stable et une largeur de bande très faible.  
ça correspond au spectre attendu d’un **signal sinusoïdal pur** dont l’énergie est concentrée sur une seule fréquence fondamentale.  
L’ajustement du **centre frequency (CF = 1 MHz)** et du **span = 500 kHz** montre bien ce comportement : forme fine sans composantes supplémentaires.  
Lorsque le **span** est élargi (jusqu’à plusieurs dizaines de MHz), le signal reste unique et aucune harmonique n’apparaît, ok pour un sinus pur.

---

### 2. Signal carré – 1 MHz, 1 Vpp, D = 50 %  
**Image 2 :**  
Le spectre présente plusieurs **pics harmoniques** : la fondamentale à 1 MHz puis des composantes aux fréquences impaires (3, 5, 7 MHz…).  
L’amplitude de ces harmoniques diminue progressivement avec la fréquence en **1/n** ce qui correspond à la **théorie de Fourier**.  
On remarque également que les pics pairs (2, 4 MHz, etc.) sont absents, ce qui est typique d’un signal carré à rapport cyclique de 50 %.  

**Image 3 :**  
Lorsque l’on étend le **span** jusqu’à 100 MHz, on observe la **décroissance globale du spectre**.  
Les premières harmoniques dominent puis le niveau de puissance chute de façon régulière.  
due à la limitation en bande passante du signal carré réel : les hautes fréquences sont atténuées à cause des limitations du générateur et des temps de montée/descente.
---

### 3. Signal radio – réception Wi-Fi  
**Image 4 :**  
Pour cette manip on a utilisé un hotspot wifi réglé à **2.4 GHz** sur un smartphone et un s'est connecté dessus avec un second smartphone en lançant une vidéo Youtube (de durée 10h et en haute qualité, pour qu'il y ait constament des données à télécharger)
Avec l’antenne connectée et la bande réglée sur **2.3–2.5 GHz** on observe un spectre centré autour de **2.405 GHz**, caractéristique du **Wi-Fi 2.4 GHz**.  
La courbe présente une **largeur de bande d’environ 20 à 25 MHz** ok pour un canal Wi-Fi (modulation OFDM).  
Le signal fluctue en amplitude mais avec **Max Hold** on peut capturer les pics.
Ce résultat confirme la détection d’un signal wifi. en éteignant le hospot le pic perd en amplitude ce qui suggère que d'autres signaux à 2.4 GHz sont captés (Wifi, bluetooth, appareils domotiques, souris/claviers etc.)

---


