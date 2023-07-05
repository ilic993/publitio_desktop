import customtkinter
from utils.Config import Config
from tkinter import messagebox
import os
import sys
import subprocess

class Settings(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = Config()

        w = 600 # width for the Tk root
        h = 300 # height for the Tk root

        # get screen width and height
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.minsize(w, h)

        self.title("Publitio Desktop Settings")
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        container = customtkinter.CTkFrame(self, corner_radius=0, fg_color=("#FFFFFF", "#1e293b"))
        container.grid(row=0, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky="NWES")
        container.grid_rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        frame = customtkinter.CTkFrame(container, corner_radius=5, fg_color=("#f1f5f9", "#0f172a"))
        frame.grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=0, sticky="NWES")
        frame.grid_rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

        fields = customtkinter.CTkFrame(frame, fg_color="transparent")
        fields.grid(row=0, column=0, padx=10, pady=10, ipadx=0, ipady=0, sticky="NWE")
        fields.grid_rowconfigure(0, weight=1)
        fields.columnconfigure(0, weight=1)
        fields.grid_rowconfigure(1, weight=1)
        fields.columnconfigure(1, weight=1)

        api_key_label = customtkinter.CTkLabel(fields, compound="left", text="API KEY", anchor="w")
        api_key_label.grid(row=0, column=0, padx=10, pady=10, ipadx=0, ipady=0, sticky="WEN")

        self.api_key = customtkinter.CTkEntry(fields, placeholder_text="API KEY", fg_color=("#FFFFFF", "#1e293b"))
        self.api_key.grid(row=0, column=1, padx=10, pady=10, ipadx=0, ipady=0, sticky="WEN")
        self.api_key.insert(0, self.config.readSetting('api_key'))

        api_secret_label = customtkinter.CTkLabel(fields, compound="left", text="API SECRET", anchor="w")
        api_secret_label.grid(row=1, column=0, padx=10, pady=10, ipadx=0, ipady=0, sticky="WEN")

        self.api_secret = customtkinter.CTkEntry(fields, placeholder_text="API SECRET", fg_color=("#FFFFFF", "#1e293b"))
        self.api_secret.grid(row=1, column=1, padx=10, pady=10, ipadx=0, ipady=0, sticky="WEN")
        self.api_secret.insert(0, self.config.readSetting('api_secret'))


        save = customtkinter.CTkButton(container, text="Save", command=self.saveSettings, anchor="CENTER")
        save.grid(row=2, column=0, padx=10, pady=(0, 10), columnspan=2, sticky="E")

        close = customtkinter.CTkButton(container, text="Close", command=self.closeSettings, anchor="CENTER", width=100)
        close.grid(row=2, column=0, padx=10, pady=(0, 10), columnspan=2, sticky="W")

    def closeSettings(self):
        self.destroy()

    def saveSettings(self):
        api_key = self.api_key.get()
        api_secret = self.api_secret.get()

        self.config.changeSetting('api_key', api_key)
        self.config.changeSetting('api_secret', api_secret)

        messagebox.showinfo("Success", "Settings saved!")
        self.restart_application()

    def restart_application(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)
        