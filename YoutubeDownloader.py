from pytube import *


def load_playlist(playlist_url: str):
    playlist = Playlist(playlist_url)
    return playlist.video_urls, playlist


def download_high_resolution(urls: list, path: str, playlist: Playlist, start_from: int):
    current_video_index = 0

    def download_info(_, __, size_remaining):
        print(f"\r[+] Downloading {video.title} ({current_video_index}/{len(urls)}) high resolution"
              f"({video.streams.get_highest_resolution().filesize - size_remaining}/"
              f"{video.streams.get_highest_resolution().filesize})", end="")

    for video_url in urls:
        current_video_index += 1
        if current_video_index >= start_from:
            try:
                video = YouTube(video_url, download_info)
                print()
                video.streams.get_highest_resolution().download(path)
            except Exception as e:
                print(f"[-] Exception raised {e} ({current_video_index}/{len(urls)})")
    print(f"[+] playlist {playlist.title} successfully downloaded")


