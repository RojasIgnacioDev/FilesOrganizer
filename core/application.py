import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from core.serialization import serialize
from core.configmanager import ConfigManager
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

    def _setup_window(self):
        self.title("File Organizer")
        self.geometry(f"{self.MIN_WIDTH}x{self.MIN_HEIGHT}")
        self.minsize(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.maxsize(self.MAX_WIDTH, self.MAX_HEIGHT)

    def _setup_widgets(self):
        # Left frame
        ### The frame where the the buttons are
        self.left_frame = ttk.Frame(self)
        self.left_frame.pack(side="left", **self.FRAME_PACKING)
        self.left_frame.rowconfigure(0, weight=1)
        self.left_frame.rowconfigure(1, weight=2)
        self.left_frame.rowconfigure(2, weight=1)
        self.left_frame.columnconfigure(0, weight=1)
        
        # The frame where it shows the workspaces
        self.right_frame = ttk.Frame(self)
        self.right_frame.pack(side="right", **self.FRAME_PACKING)

        ttk.Separator(self.left_frame, orient="horizontal").grid(column=0, row=0, ipady=40)
        ttk.Separator(self.left_frame, orient="horizontal").grid(column=0, row=5, ipady=40)

        # Organize Button
        ### The button that organizes the files when it is pressed
        self.organize_button = ttk.Button(self.left_frame)
        self.organize_button.configure(text="Organize")
        self.organize_button.grid(column=0, row=1, sticky=tk.NSEW)

        # New Workspace Button
        ### The button that creates a new workspace to be organized
        self.new_workspace_button = ttk.Button(self.left_frame)
        self.new_workspace_button.configure(text="New Workspace")
        self.new_workspace_button.grid(column=0, row=2, sticky=tk.NSEW)
        
        # Vertical Separator
        ### The separator that is in the middle of the window
        self.separator = ttk.Separator(self, orient="vertical")
        self.separator.pack(side="left", **self.FRAME_PACKING)

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
            raise NotImplementedError()
            
            

            

