import customtkinter

class App:
    def createApp(self):
        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        app = customtkinter.CTk()
        w = 1100 # width for the Tk root
        h = 580 # height for the Tk root

        # get screen width and height
        ws = app.winfo_screenwidth() # width of the screen
        hs = app.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen 
        # and where it is placed
        app.geometry('%dx%d+%d+%d' % (w, h, x, y))
        app.minsize(w, h)

        return app