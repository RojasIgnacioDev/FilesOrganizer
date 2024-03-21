import tkinter as tk
from tkinter import ttk

import src.constants as constants


class Application(tk.Frame):
    """
    The Application class creates the UI components
    """
    MIN_WIDTH = 400
    MIN_HEIGHT = 300

    MAX_WIDTH = 600
    MAX_HEIGHT = 450

    def __init__(self, parent=tk.Tk()):
        tk.Frame.__init__(self, parent, padx=8, pady=8)

        # The main window configuration
        self.parent = parent
        self.parent.title("File Organizer")
        self.parent.geometry(f"{self.MIN_WIDTH}x{self.MIN_HEIGHT}")
        self.parent.minsize(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.parent.maxsize(self.MAX_WIDTH, self.MAX_HEIGHT)
        self.pack(expand=True, fill="both")

        # Workspaces Tree
        self.workspaces_tree = ttk.Treeview(self, height=4)
        self.workspaces_tree.pack(side="top", expand=True, fill="both")
        self.workspaces_tree["columns"] = ("Status")
        self.workspaces_tree.heading("#0", text="Workspaces")
        self.workspaces_tree.heading("Status", text="Status")
        self.workspaces_tree.insert(
            "", tk.END, text="Downloads", values=["Organized"])

        # New Workspace Button
        self.new_workspace_button = ttk.Button(
            self,
            text="New Workspace",
        )
        self.new_workspace_button.pack(side="top", expand=True, fill="both")

        # Organize Button
        self.organize_button = ttk.Button(
            self,
            text="Organize",
        )
        self.organize_button.pack(side="top", expand=True, fill="both")

        # Sort Into Folders Checkbox
        self.sort_subfolders_value = tk.BooleanVar()
        self.sort_subfolders = ttk.Checkbutton(
            self,
            text="Sort Into Subfolders",
            offvalue=2,
            variable=self.sort_subfolders_value
        )
        self.sort_subfolders.pack(side="top", expand=True, fill="both")

        ########################################################################

        for child in self.winfo_children():
            child: tk.Widget
            child.pack(pady=4)
