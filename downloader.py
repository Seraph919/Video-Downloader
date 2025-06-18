from yt_dlp import YoutubeDL
import os

def download(urls, audio_only=False, output_dir='downloads', resolution='1080'):
    os.makedirs(output_dir, exist_ok=True)

    if audio_only:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s')
        }
    else:
        video_format = f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]/best'
        ydl_opts = {
            'format': video_format,
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s')
        }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)
