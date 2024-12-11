# Basic Trading Bot

Un bot de trading de crypto-monnaies basique basé sur l'utlisation de la bibliothèque ccxt, conçu pour analyser les marchés, générer des signaux d'achat et de vente basés sur des indicateurs simples, et permettre un backtesting complet des stratégies. 

## Fonctionnalités

- **Analyse Technique** :
  - Calcul du RSI (Relative Strength Index) pour détecter les zones de surachat et de survente.
  - Support prévu pour d'autres indicateurs comme les moyennes mobiles et le MACD.

- **Stratégies de Trading** :
  - Génération de signaux d'achat/vente basés sur la donnée des indicateurs calculés.
  - Backtesting pour évaluer les performances des stratégies.

- **Visualisation des Données** :
  - Interface utilisateur interactive via Streamlit pour suivre les indicateurs et les signaux (très peu développée pour le moment).


## Structure du Projet

- **`main.py`** : Point d'entrée principal pour exécuter le bot.
- **`indicators/`** : Contient les scripts pour les indicateurs techniques (RSI, MACD, MA etc.).
- **`strategies/`** : Contient les implémentations des stratégies de trading et du backtesting.
- **`data/`** : Répertoire pour stocker les données historiques et en temps réel.
- **`visualizations/`** : Contient les scripts pour l'interface utilisateur et la visualisation.
- **`tests/`** : Tests unitaires pour valider les fonctionnalités du projet.