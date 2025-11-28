# Board test plan

| Function / Block          | Test description (procedure)                                      | Expected behavior / result                                     |
|---------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------|
| Power supply (battery / USB-C) | Alimenter le PCB en USB-C puis via batterie. Mesurer les tensions principales (3.3 V, etc.). | Tensions dans tolérance, pas d'échauffement pas court-circuit. |
| ESP32 core power          | Vérifier V_alim de l'ESP32                                         | alimenté correctement?                                          |
| GPS module power          | Mesurer la tension VCC/GND du GPS.                                 | alimenté correctement, consommation ok.                         |
| LoRa module power         | Mesurer la tension VCC/GND du RFM95.                               | correctement alimenté, pas de surconsommation.                  |
| RF path 868 MHz           | Vérifier la continuité entre sortie RF et SMA + absence de court-circuit. | Chemin RF continu, aucune résistance anormale vers GND.        |
| Antenna connector         | Connecter une antenne 868 MHz commerciale.                         | Connexion mécanique et électrique correcte.                     |
| ESP32 boot / flashing     | Flasher le firmware et vérifier les logs série.                    | Flash OK, messages visibles sur port série.                     |
| GPS UART communication    | Lire les trames NMEA sur le port série.                             | Trames NMEA ok                                                  |
| GPS satellite acquisition | Sortir le PCB, attendre fix GPS.                                   | Fix 3D, >4 satellites, coordonnées valides.                     |
| LoRa TX basic             | Envoyer "Hello from 5MEO" avec la lib LoRa.                        | Transmission OK, comportement normal.                           |
| LoRa link test            | Test point-to-point avec gateway.                                  | Paquets reçus, RSSI/SNR cohérents.                              |
| LoRa range / robustness   | Tester la portée en augmentant la distance.                        | Réception stable jusqu'à quelle distance                        |
| LoRa + GPS data           | Envoyer les coordonnées GPS via LoRa.                              | Coordonnées reçues correctes.                                   |
| Wi-Fi / BLE test          | Scanner des réseaux Wi-Fi ou advertising BLE.                      | Réseaux détectés ou carte visible.                              |
| Global current consumption | Mesurer le courant en veille / GPS / LoRa TX.                     | Facultatif                                                      |

