from ui.App import App
from ui.SettingsWarning import SettingsWarning
from ui.FileList import FileList
from ui.Header import Header
from utils.Config import Config

def main(): 
    root = App()
    config = Config()
    
    Header(root)

    if config.checkKeys():
        FileList(root)
    else:
        SettingsWarning(root)

    root.mainloop()

if __name__ == '__main__':
    main()