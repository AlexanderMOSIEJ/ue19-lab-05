# Application pour afficher le  classement des 5  premières cryptomonnaies
## Description du programme
Ce script récupère les 5 premières cryptomonnaies du marché via l'API CoinLore
et affiche leur nom, symbole et prix en USD.
## Fonctionnalités 
- Récupère les données des cryptomonnaies à partir de l'API CoinLore.
- Affiche le classement des 5 premières cryptomonnaies avec leur prix en USD.
## Prérequis
- Avoir Python version 3.x
- Avoir la fonction pip
## Façon 1) Installation et exécution du programme sur cmd
### 1. Clonez le dépôt sur votre machine :
- git clone https://github.com/AlexanderMOSIEJ/ue19-lab-05.git
- cd ue19-lab-05
### 2. Installer les différentes dépendances avec :
- pip install -r requirements.txt
### 3. Lancer le programme avec :
- python app.py
## Façon 2) Construction de l'image Docker et exécuter le programme
### clonner le programme :
- git clone https://github.com/AlexanderMOSIEJ/ue19-lab-05.git
- cd ue19-lab-05
### Construction :
- docker build -t ue19-lab-05 .
### Exécution :
- docker run --rm ue19-lab-05
