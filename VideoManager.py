from pytube import YouTube
from bs4 import BeautifulSoup
from requests import *


def load_video_streams(url: str):
    video = YouTube(
        url,
        on_progress_callback
    )
    print(BeautifulSoup(get(url).text, "html.parser"))
    # video.streams.get_highest_resolution().download(".")


def download_video(url: str, stream):
    video = YouTube(url)


def on_progress_callback(any, byte, int):
    print(int)


# load_video_streams("https://www.youtube.com/watch?v=SFUngC51-z4")


