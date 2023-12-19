import customtkinter as ctk
from pytube import YouTube
import os
from pathlib import Path
import shutil

window = ctk.CTk()
window.title("Atreides-Video-Downloader")
window.geometry("500x350")

def video_downloader():
    file_name = 'Video_Downloader_Output'
    os.chdir('C:\\Users\\user\\Documents\\')
    Path(file_name).mkdir(exist_ok=True)

    link = url.get()
    yt = YouTube(link)
    print(yt.title)
    title_string.set(yt.title)
    view_string.set(yt.views)
    yd = yt.streams.get_highest_resolution()
    yd.download('C:\\Users\\user\\Documents\\Video_Downloader_Output')

title = ctk.CTkLabel(master = window, 
                     text = 'Atreides Video Downloader', 
                     font = ('calibri', 24, 'bold'))
title.pack()

download_frame = ctk.CTkFrame(master = window)
url = ctk.StringVar()
url_entry = ctk.CTkEntry(master = download_frame, textvariable = url)
entry_button = ctk.CTkButton(master = download_frame, text = "download", command = video_downloader)
download_frame.pack(pady = 10)
url_entry.pack(side = 'left', padx = 10)
entry_button.pack()

information_frame = ctk.CTkFrame(master = window)
title_string = ctk.StringVar()
title_label = ctk.CTkLabel(
    master = information_frame,
    text = 'title',
    font = ('calibri', 10),
    textvariable = title_string
)
view_string = ctk.StringVar()
view_label = ctk.CTkLabel(
    master=information_frame,
    text='views',
    font=('calibri', 10),
    textvariable=view_string
)

information_frame.pack()
title_label.pack()
view_label.pack()


window.mainloop()