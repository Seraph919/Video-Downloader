from yt_dlp import YoutubeDL
import os
import contextlib
import sys

@contextlib.contextmanager
def suppress_output():
    with open(os.devnull, 'w') as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

def header():
    print("\033[31m")
    print("  ▘ ▌      ▄        ▜      ▌    ")
    print("▌▌▌▛▌█▌▛▌▄▖▌▌▛▌▌▌▌▛▌▐ ▛▌▀▌▛▌█▌▛▘")
    print("▚▘▌▙▌▙▖▙▌  ▙▘▙▌▚▚▘▌▌▐▖▙▌█▌▙▌▙▖▌ ")
    print("\033[0m")

def download(urls, audio_only, output_dir='downloads', resolution='1080'):
    os.makedirs(output_dir, exist_ok=True)

    if audio_only == True:
        ydl_opts = {
            'ffmpeg_location': './ffmpeg-7.0.2-amd64-static/',
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
            'ffmpeg_location': './ffmpeg-7.0.2-amd64-static/',
            'format': video_format,
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s')
        }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

def exitError(str):
    print("\033[31m")
    print("Error\033[0m")
    if (str):
        print(str)
        print("Valid options:")
        print("  -1080p")
        print("  -720p")
        print("  -480p")
        print("  -360p")
    else:
        print("Wrong Argument Type")
    exit(1)
