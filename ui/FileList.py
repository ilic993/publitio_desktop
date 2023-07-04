import customtkinter
import threading
import requests
from PIL import Image

class FileList:
    def __init__(self, master):
        self.master = master

        container = customtkinter.CTkFrame(self.master, corner_radius=0, fg_color=("#f1f5f9", "#0f172a"))
        container.grid(row=1, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky="NSEW")
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=100)
        container.grid_rowconfigure(0, weight=1)

        folder_container = customtkinter.CTkScrollableFrame(container, corner_radius=0, fg_color=("#f1f5f9", "#0f172a"))
        folder_container.grid(row=0, column=0, padx=0, pady=(5, 10), ipadx=0, ipady=0, sticky="NSEW")
        folder_container.columnconfigure(0, weight=1)

        for i in range(10):
            folder = customtkinter.CTkButton(folder_container, text="Folder 1", cursor="hand2", fg_color=("#ffffff", "#1e293b"), text_color=("#000000", "#ffffff"), hover_color=("#3b8ed0", "#36719f"))
            folder.grid(row=i, column=0, padx=10, pady=5, sticky="WSNE")

        file_container = customtkinter.CTkScrollableFrame(container, corner_radius=0, fg_color=("#f1f5f9", "#0f172a"))
        file_container.grid(row=0, column=1, padx=0, pady=0, ipadx=0, ipady=0, sticky="NSEW")
        file_container.columnconfigure(0, weight=1)

        for i in range(20):
            file = customtkinter.CTkFrame(file_container, height=50, corner_radius=0, fg_color="BLUE")
            if(i%2==0):
                file.configure(fg_color=("#f1f5f9", "#0f172a"))
            else:
                file.configure(fg_color=("#ffffff", "#1e293b"))
            file.grid_rowconfigure(i, weight=1000)
            file.grid(row=i, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky="EW")

            checkbox = customtkinter.CTkCheckBox(master=file, text="", width=20)
            checkbox.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="W")

            thumbnail = customtkinter.CTkLabel(file, compound="left", text="Example file 1", height=35, corner_radius=1)
            thumbnail.grid(row=0, column=2, padx=(10, 20), pady=0, sticky="WSNE")

            size = customtkinter.CTkLabel(master=file, text="36 MB", compound="left", font=customtkinter.CTkFont(size=12, weight="normal"))
            size.grid(row=0, column=3, padx=(10, 10), pady=10, sticky="W")

            size = customtkinter.CTkLabel(master=file, text="20-Jun-2023 10:06", compound="left", font=customtkinter.CTkFont(size=12, weight="normal"))
            size.grid(row=0, column=4, padx=(10, 10), pady=10, sticky="W")

            size2 = customtkinter.CTkLabel(master=file, text="20-Jun-2023 10:06", compound="left", font=customtkinter.CTkFont(size=12, weight="normal"))
            size2.grid(row=0, column=5, padx=(10, 20), pady=10, sticky="E")

            file.columnconfigure(3, weight=1)
            file.columnconfigure(4, weight=1)
            file.columnconfigure(5, weight=1)

            #row=0 column=1
            thread = threading.Thread(target=self.display_image_from_url, args=("https://media.publit.io/file/w_300,h_200,c_fill/Jedva-Skrpeni-4k.jpg", file, i))
            thread.start()

    def display_image_from_url(self, image_url, container, i):
        image = Image.open(requests.get(image_url, stream=True).raw)
        image.resize((35,35) , Image.NEAREST)
        photo = customtkinter.CTkImage(image, size=(35,35))
        thumbnail = customtkinter.CTkLabel(container, image=photo, compound="left", text="", height=35, corner_radius=1)
        thumbnail.grid(row=0, column=1, padx=0, pady=0, sticky="WSNE")
