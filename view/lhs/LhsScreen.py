import customtkinter as ctk
from tkinter import messagebox as ms
from PIL import ImageTk, Image

from view.lhs.components.SearchEntry import search_entry


def lhs_screen(
        window: ctk.CTk,
        width: int,
        height: int
):
    # variables
    search_type = ctk.StringVar(window, "select", "variable that holds the search type")
    search_keyword = ctk.StringVar(window, "", "variable that holds the search keyword")

    # lhs screen code block
    lhs_frame = ctk.CTkScrollableFrame(window, border_width=1, width=width, height=height)
    lhs_frame.grid(row=0, column=0, padx=5, pady=5)

    text_view = ctk.CTkLabel(lhs_frame, text="Search Type", anchor="w")
    text_view.grid(row=0, column=0, padx=10, pady=(10, 3))

    combo_box = ctk.CTkComboBox(lhs_frame, values=["Playlist", "video", "Video ID", "Playlist Id", "Keyword search"],
                                width=int(width/1.5), variable=search_type)
    combo_box.grid(row=0, column=1, padx=(10, 5), pady=(10, 3))

    search_entry(lhs_frame, width=int(width/1.5), search_keyword=search_keyword)

    image = Image.open("/home/master/Downloads/search_icon.png")
    image = image.resize((30, 30))
    image = ImageTk.PhotoImage(image)
    search_button = ctk.CTkButton(lhs_frame, text="Search", image=image, anchor="w", command=lambda :search(search_type, search_keyword))
    search_button.grid(row=2, column=1, padx=(120, 10), pady=10)

    # tabs section
    tabs_info_label = ctk.CTkLabel(lhs_frame, text="Tabs", anchor="w", width=int(width/1.1), font=("roboto", 24))
    tabs_info_label.grid(row=3, column=0, columnspan=2, pady=(50, 0))

    # downloads tab button
    downloads_tab_button = ctk.CTkButton(lhs_frame, text="Downloads", width=int(width/1.1))
    downloads_tab_button.grid(row=4, column=0, columnspan=2, padx=10, pady=(15, 0))
    # bookmarks tab button
    bookmarks_tab_button = ctk.CTkButton(lhs_frame, text="Bookmarks", width=int(width / 1.1))
    bookmarks_tab_button.grid(row=5, column=0, columnspan=2, padx=10, pady=(15, 0))


def search(search_type: ctk.StringVar, search_keyword: ctk.StringVar):
    search_type = search_type.get()
    search_keyword = search_keyword.get()
    if search_type == "select":
        ms.showwarning("warning tab", f"searchType = {search_type}")
    elif search_keyword == "":
        ms.showwarning("warning tab", f"\"search_keyword\" Empty")
    else:
        ms.showinfo("info tab", f"searchType = {search_type} search_keyword = {search_keyword.get()}")
