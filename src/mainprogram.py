import tkinter as tk
from tkinter import ttk


class MainProgram(tk.Frame):
    """
    The MainProgram joins every individual UI component into the the main UI
    """
    def __init__(self, parent=tk.Tk(), title="MainProgram", *args, **kwargs):
        tk.Frame.__init__(self, parent, padx=10, pady=10, *args, **kwargs)
        
        self.parent = parent
        self.parent.title(title)
    
    def run(self):
        self.parent.mainloop()

        
# “if,” “and,” “or,” or “but.”