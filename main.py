from ui.App import App
from ui.UIButtons import UIButtons
from ui.FileList import FileList
from ui.Header import Header

def main(): 
    root = App()
    root = root.createApp()

    root.title("Publitio Desktop")
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1000)
    root.columnconfigure(0, weight=1)

    Header(root)

    # if API_KEY & API_SECRET are not set:
    # UIButtons(root)
    # else:

    FileList(root)

    root.mainloop()

if __name__ == '__main__':
    main()