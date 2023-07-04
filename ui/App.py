import customtkinter
from utils.Config import Config
from ui.Settings import Settings

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        config = Config()
        theme = config.readSetting('theme')
        customtkinter.set_appearance_mode(theme)  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        w = 1100 # width for the Tk root
        h = 580 # height for the Tk root

        # get screen width and height
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen 
        # and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.minsize(w, h)

        self.title("Publitio Desktop")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1000)
        self.columnconfigure(0, weight=1)

        self.toplevel_window = None


    def openSettings(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Settings(self)  # create window if its None or destroyed
            self.toplevel_window.after(10, self.toplevel_window.lift)
        else:
            self.toplevel_window.focus()  # if window exists focus it
