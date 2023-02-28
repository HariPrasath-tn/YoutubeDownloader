import customtkinter as ctk


def search_entry(
        parent,
        width: int,
        search_keyword: ctk.StringVar
):
    search_label = ctk.CTkLabel(parent, text="Search")
    search_label.grid(row=1, column=0, pady=(30, 0))
    search_entry_field = ctk.CTkEntry(parent, width=width, textvariable=search_keyword, placeholder_text="Search")
    search_entry_field.grid(row=1, column=1, columnspan=2, padx=5, pady=(30, 0))
