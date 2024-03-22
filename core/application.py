import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from core.serialization import serialize
from core.configmanager import ConfigManager
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

        self.parent.bind("<FocusOut>", self.configure_tree)

        # Workspaces Tree
        self.workspaces_tree = ttk.Treeview(self, height=4)
        self.workspaces_tree.pack(side="top", expand=True, fill="both")
        self.workspaces_tree["columns"] = ("Status")
        self.workspaces_tree.heading("#0", text="Workspaces")
        self.workspaces_tree.heading("Status", text="Status")
        #self.workspaces_tree.insert(
        #    "", tk.END, text="Downloads", values=["Organized"])

        # New Workspace Button
        self.new_workspace_button = ttk.Button(
            self,
            text="New Workspace",
            command=lambda: self.Events.on_new_workspace_click(self)
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
        
        self.configure_tree()

    def configure_tree(self):
        self.workspaces_tree.delete(*self.workspaces_tree.get_children())

        manager = ConfigManager()
        user_config = manager.user_config()
        workspaces = manager.workspaces(user_config)

        for workspace in workspaces:
            workspace_name = workspace["name"]
            workspace_is_organized = manager.is_workspace_organized(user_config, workspace_name)
            status = "Organized" if workspace_is_organized else "Not Organized"
            self.workspaces_tree.insert(
            "", tk.END, text=workspace_name, values=[str(status)])

    
    class Events:
        @staticmethod
        def on_new_workspace_click(app):
            root = tk.Toplevel()
            root.withdraw()

            manager = ConfigManager()
            user_config = manager.user_config()
            directory_path = filedialog.askdirectory()
            
            manager.workspace(user_config, directory_path, "")

            app.configure_tree()
            root.destroy()
        
        @staticmethod
        def on_focus_out():
            pass
            
            

            

