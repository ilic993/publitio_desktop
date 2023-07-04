from ui.App import App
from ui.UIButtons import UIButtons
from ui.FileList import FileList
from ui.Header import Header
from utils.Config import Config

def main(): 
    root = App()

    Header(root)

    config = Config()

    if config.checkKeys():
        FileList(root)
    else:
        UIButtons(root)

    root.mainloop()

if __name__ == '__main__':
    main()