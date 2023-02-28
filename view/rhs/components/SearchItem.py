import customtkinter as ctk
import pytube as tube
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO


def video_item(
        parent,
        thumbnail_url: str,
        title: str,
        channel_name: str,
        streams: tube.StreamQuery,
        width: int
):
    # search item frame
    item_frame = ctk.CTkFrame(parent, width=width)
    item_frame.pack()

    u = urlopen(thumbnail_url)
    raw_data = u.read()
    u.close()

    image = Image.open(BytesIO(raw_data))
    image = ctk.CTkImage(image, size=(120, 120))
    image_view = ctk.CTkLabel(item_frame, image=image, text="")
    image_view.grid(row=0, column=0, rowspan=4)

    title = ctk.CTkLabel(item_frame, text=title, width=width - 125, font=("roboto", 28, "bold"), anchor="w")
    title.grid(row=0, column=1, columnspan=2, padx=10)

    channel_name = ctk.CTkLabel(item_frame, text=channel_name, width=width - 125, anchor="w")
    channel_name.grid(row=1, column=1, padx=10)

    streams_filter = {}
    for stream in streams:
        if stream.type == "video":
            streams_filter[f"{stream.resolution}({stream.mime_type.split('/')[1]})" +
                           " " * (15 - len(stream.mime_type.split('/')[1])) + f"{stream.filesize_mb} MB"
                           ] = stream.itag
        elif stream.type == "audio":
            streams_filter[f"{stream.abr}({stream.audio_codec})" + " " * (15 - len(stream.audio_codec)) +
                           f"{stream.filesize_mb} MB"
                           ] = stream.itag  
    format_listbox = ctk.CTkComboBox(item_frame, values=list(streams_filter.keys()), font=("roboto", 16))
    format_listbox.grid(row=2, column=1, padx=(10, width - 250))


screen = ctk.CTk()
video = tube.YouTube("https://www.youtube.com/watch?v=nhea4gisvsM")
channel = tube.Channel(video.channel_url)
video_item(
    screen,
    video.thumbnail_url,
    video.title,
    channel.channel_name,
    video.streams,
    1100)
screen.mainloop()
