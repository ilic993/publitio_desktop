import customtkinter
import os
from PIL import Image
import webbrowser
from utils.Config import Config

class Header:
    def __init__(self, master):
        self.master = master

        # Top header frame
        header_frame = customtkinter.CTkFrame(self.master, corner_radius=0, height=50, fg_color=("#FFFFFF", "#1e293b"))
        header_frame.grid(row=0, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky="NWE")
        header_frame.columnconfigure(0, weight=1)

        # Publitio branding
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', "images")
        logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "publitio-b.png")), size=(44, 32))
        publitio_branding = customtkinter.CTkLabel(header_frame, text="  Publitio Desktop", image=logo_image, compound="left", font=customtkinter.CTkFont(size=15, weight="bold"), cursor="hand2")
        publitio_branding.bind("<Button-1>", lambda e:webbrowser.open_new_tab("https://publit.io"))

        # Theme switcher
        theme_switcher = customtkinter.CTkOptionMenu(header_frame, values=["Light", "Dark", "System"], width=100, command=self.changeTheme)
        self.config = Config()
        theme = self.config.readSetting('theme')
        theme_switcher.set(theme)

        publitio_branding.grid(row=0, column=0, sticky="W", padx=10, pady=10)
        theme_switcher.grid(row=0, column=0, sticky="E", padx=(10, 50), pady=10)

        settings_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "settings-b.png")), size=(18, 18))
        settings = customtkinter.CTkButton(header_frame, text="", image=settings_image, command=self.openSettings, anchor="CENTER", width=30)
        settings.grid(row=0, column=0, sticky="E", padx=10, pady=10)

    def changeTheme(self, newTheme):
        self.config.changeSetting('theme', newTheme)
        customtkinter.set_appearance_mode(newTheme)

    def openSettings(self):
        self.master.openSettings()

