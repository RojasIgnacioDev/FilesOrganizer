import tkinter as tk

class OrganizeButton(tk.Button):
    """
    The OrganizeButton arranges the files by its type putting them into different folders.
    """
    def __init__(self, parent, command, *args, **kwargs):
        tk.Button.__init__(
            self, 
            parent, 
            text="Organize",
            command=command,
            *args, 
            **kwargs)

        
    