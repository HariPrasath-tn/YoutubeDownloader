import customtkinter as tk

from view.lhs.LhsScreen import lhs_screen
from view.rhs.RhsScreen import rhs_screen

YoutubeDownloaderWindow = tk.CTk()
YoutubeDownloaderWindow.title("Youtube Downloader")
YoutubeDownloaderWindow.resizable(False, False)
parent_width, parent_height = 1600, 900


lhs_screen(
    YoutubeDownloaderWindow,
    parent_width - 1220,
    parent_height - 20
)

rhs_screen(
    YoutubeDownloaderWindow,
    parent_width - 420,
    parent_height
)

YoutubeDownloaderWindow.mainloop()
