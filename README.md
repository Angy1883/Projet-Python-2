echo > requirements.txt
# System Monitoring

Un outil de surveillance système qui collecte et affiche des métriques de performance, des informations réseau, des données météorologiques et des logs système.

## Description

System Monitoring est une application Python qui fournit une solution complète pour la surveillance de votre système. Elle collecte et affiche des informations essentielles comme l'utilisation du CPU, la mémoire RAM, l'espace disque, les données météorologiques locales, les logs système et les statistiques réseau.

## Fonctionnalités

- Surveillance en temps réel des métriques système (CPU, RAM, espace disque)
- Identification des trois processus consommant le plus de ressources CPU
- Collecte des statistiques réseau (paquets envoyés/reçus)
- Affichage des données météorologiques via une API externe
- Enregistrement quotidien des logs système

## Structure du projet

Le projet est composé de cinq modules principaux :

- **main.py** : Module principal qui coordonne l'ensemble des fonctionnalités
- **system_monitor.py** : Collecte et analyse les métriques système (CPU, RAM, disque, processus)
- **weather_api.py** : Interface avec l'API météorologique pour récupérer les données locales
- **logger.py** : Gestion et enregistrement des logs système dans un fichier
- **display.py** : Interface utilisateur pour présenter les informations collectées

## Prérequis

- Python 3.6 ou supérieur
- Connexion Internet (pour les données météorologiques)
- Permissions système adéquates pour accéder aux métriques système

## Installation

1. Clonez ce dépôt :
   ```
   git clone https://github.com/username/system-monitoring.git
   cd system-monitoring
   ```

2. Installez les dépendances requises :
   ```
   pip install -r requirements.txt
   ```

## Utilisation

1. Lancez l'application via le module principal :
   ```
   python main.py
   ```

2. L'interface affichera les métriques système et les données météorologiques en temps réel.

3. Les logs sont automatiquement enregistrés quotidiennement dans le répertoire `logs/`.

## Configuration

Vous pouvez modifier les paramètres de l'application en éditant le fichier `config.py` :

- Intervalle de rafraîchissement des données
- Emplacement pour l'API météo
- Format et destination des fichiers de log

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à soumettre des pull requests ou à ouvrir des issues pour améliorer ce projet.

## Auteurs

- Axel Gillet
- Angélique Quilez

