import tkinter as tk

from src.core.foldercontentgiver import FolderContentGiver
from src.core.filemover import FileMover
from src import constants

class OrganizeButton(tk.Button):
    """
    The OrganizeButton arranges the files by its type putting them into different folders.
    """
    TEXT = "Organize"

    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)

        self.configure(text=self.TEXT)
        self.configure(command=self.on_button_click)
        self.configure(padx=16, pady=4)
        self.configure()
        self.grid(column=2, row=2)
        
    def on_button_click(self):
        giver = FolderContentGiver(constants.DOWNLOADS_FOLDER_PATH)
        files = giver.files(format=constants.DirectoryType.ABSOLUTE_PATH)
    