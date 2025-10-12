import yt_dlp

# Define options (same as CLI flags, but in dict form)
ydl_opts = {
    'format': 'best',  # download best video+audio
    'outtmpl': '%(title)s.%(ext)s',  # name of the output file
}

url = 'https://www.youtube.com/watch?v=VIDEO_ID'

# Use yt-dlp with the options
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
