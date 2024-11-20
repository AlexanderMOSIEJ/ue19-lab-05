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
## Installation et exécution du programme
### 1. Clonez le dépôt sur votre machine :
- https://github.com/AlexanderMOSIEJ/ue19-lab-05.git
### 2. Installer les différentes dépendances avec :
- pip install -r requirements.txt
### 3. Lancer le programme avec :
- python app.py
## Construction de l'image Docker et exécuter le contenu
### Construction :
- docker build -t ue19-lab-05 .
### Exécution :
- docker run --rm ue19-lab-05
