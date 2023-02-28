import customtkinter as ctk


def rhs_screen(
        window: ctk.CTk,
        width: int,
        height: int,
        search_type_value: dict
):
    rhs_screen_frame = ctk.CTkFrame(window, border_width=1, width=width, height=height)
    rhs_screen_frame.grid(row=0, column=1)

    if search_type_value.keys()[0] == "keyword":
        Keyword_search_result()
