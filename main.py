# This is a sample Python script.
from YoutubeDownloader import load_playlist, download_high_resolution


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def __init__():
    (urls, playlist) = load_playlist("https://youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV")
    download_high_resolution(urls, "/home/master/Downloads/tkinter/", playlist, 40)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    __init__()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#test
print("hello")