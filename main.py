from downloader import download

print("\033[31m")
print("  ▘ ▌      ▄        ▜      ▌    ")
print("▌▌▌▛▌█▌▛▌▄▖▌▌▛▌▌▌▌▛▌▐ ▛▌▀▌▛▌█▌▛▘")
print("▚▘▌▙▌▙▖▙▌  ▙▘▙▌▚▚▘▌▌▐▖▙▌█▌▙▌▙▖▌ ")
print("\033[0m")
urls_input = input("Enter YouTube URL(s), separated by spaces: ").strip()
if not urls_input:
    print("No URLs entered. Exiting...")
    exit(1)

urls = urls_input.split()
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

download(urls, audio_only=audio_only, resolution=resolution)
