import customtkinter

class SettingsWarning:
    def __init__(self, master):
        self.master = master

        container = customtkinter.CTkFrame(self.master, corner_radius=0, fg_color=("#f1f5f9", "#0f172a"))
        container.grid(row=1, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky="NSEW", columnspan=2)
        container.columnconfigure(0, weight=1000)
        container.grid_rowconfigure(1, weight=1)

        labelText = "Please input your valid API secret and API key.\n\n\n\n\n"
        label = customtkinter.CTkLabel(container, text=labelText, compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        label.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        button = customtkinter.CTkButton(container, text="Settings", command=self.openSettings, anchor="CENTER")
        button.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        button = customtkinter.CTkButton(container, text="Exit", width=70, command=self.quitButtonHandle, anchor="ES")
        button.grid(row=2, column=1, padx=10, pady=10)

    def quitButtonHandle(self):
        quit()

    def openSettings(self):
        self.master.openSettings()
