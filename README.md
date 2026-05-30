# EduBot — Chatbot IA pour étudiants ingénieurs

## Description
EduBot est un assistant pédagogique intelligent qui répond aux questions 
de cours des étudiants en école d'ingénieurs, propulsé par Llama 3.2.

## Étudiants
- Yosr Ouali

## Technologies utilisées
- Python + Flask (serveur web)
- Llama 3.2 via Ollama (modèle génératif LLM)
- HTML / CSS / JavaScript (interface)

## Installation

### 1. Installer Ollama
Télécharger sur https://ollama.com puis lancer :
ollama pull llama3.2:1b

### 2. Installer les dépendances
pip install flask requests

### 3. Lancer Ollama
ollama serve

### 4. Lancer l'application
python app.py

### 5. Ouvrir dans le navigateur
http://127.0.0.1:5000

## Fonctionnalités
- Réponses en français adaptées au niveau ingénieur
- Sélection de matière (maths, info, IA, réseaux...)
- Historique de conversation
- Interface moderne dark mode
