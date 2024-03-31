import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from core.serialization import serialize
from core.config_manager import ConfigManager

class Application(tk.Tk):
    """
    The Application class creates the UI components
    """

    # The minimum and maximum size the window can be resized
    MIN_WIDTH = 400
    MIN_HEIGHT = 300
    MAX_WIDTH = 1280
    MAX_HEIGHT = 768

    # The frame containg the buttons
    left_frame = None
    # The frame containing the workspaces
    right_frame = None

    # The padx and pady value used for every widget
    BUTTON_CONFIG = {"master": left_frame}
    
    FRAME_PACKING = {"padx": 8, "pady": 32, "expand": True, "fill": "both"}
    BUTTON_PACKING = {"padx": 4, "pady": 16, "fill": "both"}

    def __init__(self):
        tk.Tk.__init__(self,)

        self._setup_window()
        self._setup_widgets()
        self._start_app_with_default_config()

    def _setup_window(self):
        self.title("File Organizer")
        self.geometry(f"{self.MIN_WIDTH}x{self.MIN_HEIGHT}")
        self.minsize(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.maxsize(self.MAX_WIDTH, self.MAX_HEIGHT)

    def _setup_widgets(self):
        #
        # LEFT
        #

        # Left frame
        ### The frame where the the buttons are
        self.left_frame = ttk.Frame(self)
        self.left_frame.rowconfigure(0, weight=1)
        self.left_frame.rowconfigure(1, weight=4)
        self.left_frame.rowconfigure(2, weight=1)
        self.left_frame.columnconfigure(0, weight=1)
        self.left_frame.pack(side="left", **self.FRAME_PACKING)
        
        # Organize Button
        ### The button that organizes the files when it is pressed
        self.organize_button = ttk.Button(self.left_frame)
        self.organize_button.config(text="Organize")
        self.organize_button.config(command=self.Events.on_organize_click)
        self.organize_button.grid(column=0, row=1, sticky=tk.NSEW)

        #@TODO a
        # New Workspace Button
        ### The button that creates a new workspace to be organized
        self.new_workspace_button = ttk.Button(self.left_frame)
        self.new_workspace_button.config(text="New Workspace")
        # For now, it will not be placed
        #self.new_workspace_button.grid(column=0, row=2, sticky=tk.NSEW)

        ttk.Separator(self.left_frame, orient="horizontal").grid(column=0, row=0, ipady=40)
        ttk.Separator(self.left_frame, orient="horizontal").grid(column=0, row=5, ipady=40)

        # Vertical Separator
        ### The separator that is in the middle of the window
        self.separator = ttk.Separator(self, orient="vertical")
        self.separator.pack(side="left", **self.FRAME_PACKING)

        #
        # RIGHT
        #
        
        # The frame where it shows the workspaces
        self.right_frame = ttk.Frame(self)
        self.right_frame.rowconfigure(0, weight=31)
        self.right_frame.rowconfigure(1, weight=1)
        self.right_frame.columnconfigure(0, weight=1)
        self.right_frame.pack(side="right", **self.FRAME_PACKING)

        # The Workspace TreeView
        self.workspaces_tree = ttk.Treeview(self.right_frame)
        self.workspaces_tree.grid(column=0, row=0, sticky=tk.NSEW)
        scrollbar = ttk.Scrollbar(self.right_frame)
        self.workspaces_tree.config(yscrollcommand=scrollbar.set, show="tree")

    def _start_app_with_default_config(self):
        ConfigManager().reset_user_config()

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
        def on_organize_click():
            user_config = ConfigManager.user_config()
            ConfigManager.print_workspaces(user_config)

        @staticmethod
        def on_focus_out():
            raise NotImplementedError()
            
            

            

