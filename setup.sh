#!/bin/bash

echo "🚀 Installation de Music Downloader..."

# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install flask flask-cors yt-dlp certifi

# Créer les dossiers nécessaires
mkdir -p downloads templates static

# Copier les fichiers HTML/CSS si besoin
cp index.html templates/
cp style.css static/

echo "✅ Installation terminée. Lancez l'app avec :"
echo "source venv/bin/activate && python app.py"
