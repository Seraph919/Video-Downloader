from tools import download
from tools import exitError
from tools import header
import sys

if len(sys.argv) == 1:
    header()
    urls_input = input("Enter YouTube URL(s), separated by spaces: ").strip()
    if not urls_input:
        print("No URLs entered. Exiting...")
        exit(1)

    urls = urls_input.split()
    choice = 'f'
    while choice not in "yn":
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
    download(urls.split(' '), audio_only, resolution=resolution)

elif len(sys.argv) > 4:
    valid_res = {"1080", "720", "480", "360","1080p", "720p", "480p", "360p"}
    audio_only = False
    resolution = "1080"
    if ("https:" in sys.argv[1]) :
        urls = sys.argv[1]
    else:
        exitError()
    for i in range(len(sys.argv)):
        if ("https:" in sys.argv[i]):
            urls =  urls + ' ' + sys.argv[i]
        if ("--only-audio" in sys.argv[i]):
            audio_only = True
        if ("--res=" in sys.argv[i]):
            if (sys.argv[i].split('=')[1] in valid_res):
                if 'p' in sys.argv[i].split('=')[1]:
                    resolution = sys.argv[i].split('=')[1][:-1]
                else:   
                    resolution = sys.argv[i].split('=')[1]
            else:
                print(sys.argv[i])
                exitError("Invalid Resolution")
    
    # urls = urls.split(' ')
    # header()
    # print(urls.split())
    # print(audio_only)
    # print(resolution)
    download(urls.split(' '), audio_only, resolution=resolution)
