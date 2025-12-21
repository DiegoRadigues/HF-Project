# Rapport de laboratoire : Analyseur de spectre 
**Arthur DUFOUR — Ange SIMPALINGABO — Diego de RADIGUES**

## Résultats et discussion  

![sinus1mHz900_1100MHz](https://github.com/user-attachments/assets/687cb7bc-5231-462e-a660-4f056b1b302d)

### 1. Signal sinusoïdal – 1 MHz  
**Image 1 :**  
On observe un **seul pic centré à 1 MHz** avec une amplitude stable et une largeur de bande très faible.  
ça correspond au spectre attendu d’un **signal sinusoïdal pur** dont l’énergie est concentrée sur une seule fréquence fondamentale.  
L’ajustement du **centre frequency (CF = 1 MHz)** et du **span = 500 kHz** montre bien ce comportement : forme fine sans composantes supplémentaires.  
Lorsque le **span** est élargi (jusqu’à plusieurs dizaines de MHz), le signal reste unique et aucune harmonique n’apparaît, ok pour un sinus pur.

---

### 2. Signal carré – 1 MHz, 1 Vpp, D = 50 % 
![1harmonique](https://github.com/user-attachments/assets/7ebcd83f-b455-480f-94a7-945904e3c6fd)

**Image 2 :**  
Le spectre présente plusieurs pics harmoniques : la fondamentale à 1 MHz puis des composantes aux fréquences impaires (3, 5, 7 MHz…).  
L’amplitude de ces harmoniques diminue progressivement avec la fréquence en **1/n** ce qui correspond à la **théorie de Fourier**.  
On remarque également que les pics pairs (2, 4 MHz, etc.) sont absents, ce qui est typique d’un signal carré à rapport cyclique de 50 %.  

![harminoniques](https://github.com/user-attachments/assets/a2d72a24-ba76-40a4-ab59-9aeaa153a188)

**Image 3 :**  
Lorsque l’on étend le span jusqu’à 100 MHz, on observe la **décroissance globale du spectre**.  
Les premières harmoniques dominent puis le niveau de puissance chute de façon régulière.  
Du à la limitation en bande passante du signal carré réel : les hautes fréquences sont atténuées à cause des limitations du générateur et des temps de montée/descente.

---

### 3. Signal radio – réception Wi-Fi  
<img width="761" height="456" alt="wifi" src="https://github.com/user-attachments/assets/ce563f45-c880-4648-abfb-aca29c91aafb" />


**Image 4 :**  
Pour cette manip on a utilisé un hotspot wifi réglé à **2.4 GHz** sur un smartphone et un s'est connecté dessus avec un second smartphone en lançant une vidéo Youtube (de durée 10h et en haute qualité, pour qu'il y ait constament des données à télécharger)
Avec l’antenne connectée et la bande réglée sur **2.3–2.5 GHz** on observe un spectre centré autour de **2.405 GHz**, caractéristique du **Wi-Fi 2.4 GHz**.  
La courbe présente une **largeur de bande d’environ 20 à 25 MHz** ok pour un canal Wi-Fi (modulation OFDM).  
Le signal fluctue en amplitude mais avec **Max Hold** on peut capturer les pics.
Ce résultat confirme la détection d’un signal wifi. en éteignant le hospot le pic perd en amplitude ce qui suggère que d'autres signaux à 2.4 GHz sont captés (Wifi, bluetooth, appareils domotiques, souris/claviers etc.)

![x](https://github.com/user-attachments/assets/bd1edc4b-c7bd-4e0b-a22f-646343fd815e)
Image 5 :
Le marqueur indique un pic à 93,230 MHz avec une puissance d’environ –53,09 dBm.
Cette fréquence correspond très bien à 93,2 MHz = Classic 21 (Bruxelles) dans votre liste.
On observe autour de cette porteuse une “bosse” assez large : c’est normal car une station FM occupe typiquement ~200 kHz (ordre de grandeur), et l’affichage est aussi influencé par la RBW = 300 kHz, qui a tendance à élargir visuellement les signaux.

![z](https://github.com/user-attachments/assets/78813990-de6c-4f52-8739-59dd2147b1fc)
Le marqueur indique un pic à 107,195 MHz pour environ –47,68 dBm (ici plus fort que celui de 93,23 MHz).
Dans votre liste, la fréquence 107,2 MHz correspond à Radio Vibration et aussi Radio Extra (même fréquence annoncée). Avec uniquement le spectre, on ne peut pas trancher laquelle des deux est effectivement reçue : on peut seulement dire que le pic est compatible avec une station autour de 107,2 MHz.
La petite différence entre 107,195 et 107,2 MHz est attendue (lecture au marqueur, résolution fréquentielle, RBW, etc.).

Discussion :

Les stations n’ont pas la même amplitude : cela dépend de la puissance d’émission, de la distance, des obstacles (bâtiments), et de l’orientation/position de l’antenne.

Le Max Hold met bien en évidence les stations présentes même si leur niveau varie dans le temps.

Avec un RBW de 300 kHz, on ne voit pas des détails fins ; pour “mieux dessiner” chaque station, on pourrait réduire le span autour d’une station et diminuer la RBW (ex. dizaines de kHz).


---


