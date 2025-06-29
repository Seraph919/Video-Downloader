import sys
import argparse
from halo import Halo
from tools import download
from tools import suppress_output
from tools import exitError
from tools import header


parser = argparse.ArgumentParser(
    description=None,
    usage=None,
    add_help=False
)
parser.add_argument('--help', action='store_true', help='Show this help message and exit')
args, unknown = parser.parse_known_args()

if args.help:
    header()
    print("\nUsage: main.py [urls] [--res=RESOLUTION] [--only-audio]")
    print("options:")
    print("     --res=RESOLUTION      Set the resolution (1080, 720, 480, 360)")
    print("     --only-audio          Download as MP3 (audio only)")
    sys.exit(0)

elif len(sys.argv) == 1:
    header()
    urls_input = input("Enter YouTube URL(s), separated by spaces: ").strip()
    if not urls_input:
        print("No URLs entered. Exiting...")
        exit(1)

    urls = urls_input.split()
    choice = 'd'
    while choice not in "ynYN":
        choice = input("Download as MP3 (audio only)? (y/n): ").strip().lower()
    audio_only = choice == 'y'

    resolution = '1080'
    if not audio_only:
        print("\nChoose video resolution:")
        print("  1. 1080p (default)")
        print("  2. 720p")
        print("  3. 480p")
        print("  4. 360p")
        res_choice = -1;
        while True:
            res_choice = input("Enter choice (1-4): ").strip()
            if res_choice in ['1', '2', '3', '4']:
                break
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
        resolution_map = {'1': '1080', '2': '720', '3': '480', '4': '360'}
        resolution = resolution_map.get(res_choice, '1080')
    # print(urls)
    download(urls, audio_only, resolution=resolution)

elif len(sys.argv) >= 2:
    valid_res = {"1080", "720", "480", "360","1080p", "720p", "480p", "360p"}
    audio_only = False
    resolution = "1080"
    if ("https:" in sys.argv[1]) :
        urls = sys.argv[1]
    else:
        exitError(None)
    for i in range(len(sys.argv)):
        arg = sys.argv[i]
        if "https:" in arg:
            urls =  urls + ' ' + arg
        if "--only-audio" in arg:
            audio_only = True
        if not audio_only and "--res=" in arg:
            if (arg.split('=')[1] in valid_res):
                if 'p' in arg.split('=')[1]:
                    resolution = arg.split('=')[1][:-1]
                else:   
                    resolution = arg.split('=')[1]
            else:
                exitError("Invalid Resolution")
    
    # urls = urls.split(' ')
    header()
    # print(urls.split())
    # print(audio_only)
    # print(resolution)
    spinner = Halo(text='Downloading...', spinner='dots')
    spinner.start()

    try:
        with suppress_output():
            download(urls, audio_only, resolution=resolution)
        spinner.succeed("Download complete!")
    except Exception as e:
        spinner.fail(f"Failed: {e}")
