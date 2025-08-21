import yt_dlp
import ssl
import certifi

ssl._create_default_https_context = ssl.create_default_context(cafile=certifi.where())


musiques = {
"krista marguerite": ["Lis ta bible"],
}


options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


with yt_dlp.YoutubeDL(options) as ydl:
    for artiste, titres in musiques.items():
        for titre in titres:
            recherche = f"{artiste} {titre}"
            print(f"🔎 Recherche : {recherche}")
            ydl.download([f"ytsearch1:{recherche}"])
            print(f"✅ Téléchargé : {recherche}\n")
