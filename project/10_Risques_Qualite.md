#  Gestion des risques & qualité

---

## Registre des risques

| ID | Risque | Impact | Probabilité | Plan de mitigation |
|----|--------|--------|-------------|--------------------|
| R1 | Antenne mal accordée (S11 > –10 dB) | Perte RF / faible portée | Moyen | Simu OpenEMS + tuning LC sur PCB |
| R2 | Retard fabrication PCB | Livraison bloquée | Moyen | Commander tôt (JLCPCB), prévoir 1 sem buffer |
| R3 | Bug SDK ESP32 | Retard firmware | Moyen | Tester firmware minimal tôt, log UART |
| R4 | Consommation trop élevée | Autonomie réduite | Moyen | Vérifier deep sleep dès P2, optimisation early |
| R5 | EMI hors norme | Non-conformité | Faible | Pré-scan labo, prévoir shielding option |
| R6 | Erreur schéma/footprint | PCB inutilisable | Faible | Revue pair + CI DRC/ERC headless |
| R7 | Instrumentation indispo (VNA, spectre) | Tests retardés | Moyen | Réserver matériel, prévoir créneaux backup |
| R8 | GPS sans fix stable | Démo compromise | Faible | Tester extérieur tôt, antenne active fallback |

---

## Gates qualité par phase

- **Phase 1 (PCB)**  
  -  ERC/DRC pass.  
  -  Règles JLCPCB respectées.  
  -  BOM validée.

- **Phase 2 (Firmware stub + choix antenne)**  
  -  Logs UART visibles.  
  -  Scan Wi-Fi OK.  
  -  Antenne choisie documentée.

- **Phase 3 (Antenne design)**  
  -  Simulation OpenEMS documentée.  
  -  S11 < –10 dB simulé @ 868 MHz.

- **Phase 4 (Protocoles/tests initiaux)**  
  -  Plan de test rédigé.  
  -  EMI/CEM simulation réalisée.  
  -  Firmware LoRa ping compilé.

- **Phase 5 (Tests instrumentés)**  
  -  VNA calibré.  
  -  S11 mesuré < –10 dB.  
  -  Portée LoRa > 300 m.  
  -  GPS fix < 60 s.

- **Phase 6 (Oral final)**  
  -  Rapport complet.  
  -  Présentation claire.  
  -  Démo POC fonctionnel.

---

## Checklists qualité

### DRC/DFM (à cocher avant envoi PCB)
- [ ] ERC sans erreurs bloquantes.  
- [ ] DRC passé (espacements, largeurs pistes).  
- [ ] Stackup FR4 2 couches validé.  
- [ ] Connecteurs SMA/USB footprint vérifiés.  
- [ ] Alim + découplage respecté.  
- [ ] Fichiers Gerbers vérifiés (VisualGerber).  

### Firmware
- [ ] Compilation ESP-IDF sans warning bloquant.  
- [ ] Lint/style code respecté.  
- [ ] Logs UART testés.  
- [ ] Drivers GPS/LoRa init OK.  

### Tests labo
- [ ] VNA calibré (SOLT).  
- [ ] Antenne mesurée.  
- [ ] LoRa ping OK.  
- [ ] GPS fix OK.  
- [ ] Consommation mesurée en deep sleep.  