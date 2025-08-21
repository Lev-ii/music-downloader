from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import yt_dlp
import ssl
import certifi
import os

app = Flask(__name__)
CORS(app)
ssl._create_default_https_context = ssl.create_default_context(cafile=certifi.where())

# Crée le dossier de téléchargement s'il n'existe pas
os.makedirs("downloads", exist_ok=True)

@app.route('/admin')
def admin_panel():
    files = os.listdir('downloads')
    return render_template('admin.html', files=files)

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    path = os.path.join('downloads', filename)
    if os.path.exists(path):
        os.remove(path)
        return jsonify({'message': f'{filename} supprimé'})
    return jsonify({'error': 'Fichier introuvable'}), 404

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_music():
    data = request.get_json()
    artist = data.get('artist')
    title = data.get('title')

    if not artist or not title:
        return jsonify({'error': 'Champs manquants'}), 400

    search_query = f"{artist} {title}"
    options = {
        'format': 'bestaudio/best',
        'outtmpl': f'downloads/{search_query}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([f"ytsearch1:{search_query}"])
        return jsonify({'message': f'Téléchargement réussi : {search_query}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
