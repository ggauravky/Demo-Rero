import yt_dlp

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

url = 'https://youtu.be/Wld2pSTFh_M?si=THH9cTEClrs7jMGc'

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
