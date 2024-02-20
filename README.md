# Turbo Complete Algo 🧬

Bienvenue dans la documentation du dépôt gérant l'algorithme pour le projet d'IA Turbo Complete. Ce guide fournit des informations sur la configuration, l'exécution et la contribution au code.

📜 Table des matières

- [Introduction](#introduction)
- [Construit avec](#built-with)
- [Prérequis](#prerequisites)
- [Démarrage rapide](#quick-start)
- [Configuration de l'environnement](#environment-configuration)
- [Exécuter l'application](#run-the-application)
- [Contribuer](#contributing)
- [Améliorations possibles](#to-improve)
- [Retour d'information](#feedback)

## Introduction
Ce projet sert de gestion de l'IA pour l'application AI Turbo Complete 🚀. 

## Construit avec
- Python 3
- Bibliothèques Python telles que :
  - [Flask](https://flask.palletsprojects.com/en/3.0.x/)
  - [TensorFlow](https://www.tensorflow.org/)
  - [Ollama](https://ollama.ai/)

## Prérequis
Avant d'exécuter le projet, assurez-vous d'avoir installé les éléments suivants sur votre système :

- Python 3 : le langage de programmation utilisé pour le projet.
- Pip : l'installateur de packages pour Python.
- Virtualenv : un outil pour créer des environnements Python isolés.

## Démarrage rapide

1. Clonez le dépôt

```bash
git clone https://github.com/your-username/turbo-complete-algo.git
```

2. Accédez au répertoire du projet

```bash
cd turbo-complete-algo
```

3. Installez les dépendances

```bash
pip install -r requirements.txt
```

4. Installer replicate et transformers

  ```bash
python3 -m pip install replicate
python3 -m pip install transformers
```

7. Installer et lancer Ollama en local : https://ollama.ai/download

## Configuration de l'environnement
Créez un fichier `.env.local` à la racine du projet et configurez les variables d'environnement nécessaires pour EBAY API, MONGODB :

```env
MONGODBCLIENT=***your-url***
FLASK_API_KEY=turbo_complete
OLLAMA_API_ENDPOINT=***your-url***
DATA_API_ENDPOINT=http://127.0.0.1:5001/
```

## Exécuter l'application

1. Accédez au répertoire `app/api`

2. Lancez l'API

```
naviguer jusqu'à app/adapters/controllers/image_controller

puis dans le terminal : 

```bash
python3 main.py
```

## Contribuer
Nous accueillons les contributions ! Pour contribuer au projet, suivez ces étapes :

1. Forkz le dépôt.
2. Créez une nouvelle branche : `git checkout -b feature/your-feature-name`.
3. Effectuez vos modifications et commitez-les : `git commit -m 'Ajouter une fonctionnalité'`.
4. Pushez vers la branche : `git push origin feature/your-feature-name`.
5. Soumettez une pull request.

## Améliorations possibles
Voici quelques domaines d'amélioration :

- Ajouter des tests API.
- Mettre en œuvre Docker pour faciliter l'accès à l'application.
- Améliorer la clean architecture : Principes solid

N'hésitez pas à contribuer et à aider à rendre Turbo Complete 🚀 encore meilleur !

## Retour d'information
Nous apprécions vos retours. Si vous avez des suggestions ou rencontrez des problèmes, veuillez nous le faire savoir en ouvrant une issue dans le dépôt.
