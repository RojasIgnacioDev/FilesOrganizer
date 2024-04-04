import sys
sys.path.append("F:/DATOS/Documents/Projects/Python Projects/FilesOrganizer")

import pathlib

from core.folder_content_giver import FolderContentGiver
import core.constants as constants

class ConfigManager():
    # Folder where the user config will be stored 
    DATA_DIRECTORY = pathlib.Path("data")
    # Path of the file where the user config is stored
    USER_CONFIG_PATH = pathlib.Path("userconfig.pickle")

    default_config_data = None

    # Constructor
    def __init__(self) -> None:
        self._create_default_config()

    @staticmethod
    def print_workspaces(config):
        workspaces :list= config["workspaces"]
        print("\n\n\nWorkspaces")
        for workspace in workspaces:
            name = workspace["name"]
            path = workspace["path"]
            prefix = workspace["prefix"]
            print(f"■\t{name} in {path}. Prefix = '{prefix}'")

    def workspaces(self, config):
        """
        Returns the workspaces of the given config
        """
        workspaces = config["workspaces"]
        return workspaces

    def extensions(self, config):
        """
        Returns the extensions of the given config
        """
        extensions = config["extensions"]
        return extensions
    
    @staticmethod
    def workspace(config, path, prefix):
        """
        Creates a new workspace in the config obj
        """
        if not isinstance(path, pathlib.Path):
            path = pathlib.Path(path)
        workspaces = config["workspaces"]
        workspaces.append({"name": path.name, "path": path, "prefix": prefix})
        

    @staticmethod
    def extension(config, category, formats: list):
        """
        Creates a new extension in the config obj
        """
        extensions = config["extensions"]
        extensions.append({"category": category, "formats": formats})

    @staticmethod
    def default_config():
        return ConfigManager.default_config_data

        
 
    #@NotUsed
    def folder(self, from_path: pathlib.Path, prefix_name, last_name):
        """
        Creates a folder from a specified path, making its name in base of the prefix and the last name
        """
        path = from_path / f"{prefix_name} {last_name}"
        path.mkdir(exist_ok=True)
        
    #@NotUsed
    def move_files_to_folder(self):
        raise NotImplementedError()

    #@NotImplemented
    def move_files_to_subfolder(self):
        raise NotImplementedError()

    def is_workspace_organized(self, config, workspace_name):
        workspace = [ws for ws in config["workspaces"] if ws["name"] == workspace_name].pop()
        workspace_path = workspace["path"]
        workspace_files = FolderContentGiver(workspace_path).files()
        return len(workspace_files) == 0
        
    def _user_config_exists(self):
        return self._user_config_path().exists()
    
 
    def _create_default_config(self):
        """
        Creates the default config data at the instantiation of the class object
        """
        self.default_config_data = {"extensions": [], "workspaces": []}
        # Add the extensions
        image_formats = [
            ".jpg",  # Joint Photographic Experts Group
            ".png",  # Portable Network Graphics
            "jpeg",  # JPEG format (alternative extension)
            ".webp",  # Modern format for web images
            ".tiff",  # Tagged Image File Format
            ".psd",  # Photoshop Document
            ".raw",  # High-quality image format from digital cameras
            ".bmp",  # Bitmap Image File
            ".heif",  # High Efficiency Image File Format
            ".indd",  # Adobe InDesign Document
            ".tif",  # TIFF (alternative extension)
            ".svg",  # Scalable Vector Graphics
            ".ai",   # Adobe Illustrator Artwork image
            ".eps",  # Encapsulated PostScript
        ]
        video_formats = [
            ".3g2",  # 3GPP2 multimedia file
            ".3gp",  # 3GPP multimedia file
            ".avi",  # AVI (Audio Video Interleave) file
            ".flv",  # Adobe Flash file
            ".h264",  # H.264 video file
            ".m4v",  # Apple MP4 video file
            ".mkv",  # Matroska Multimedia Container
            ".mov",  # Apple QuickTime movie
            ".mp4",  # MPEG4 video file
            ".mpg",  # MPEG (Moving Picture Experts Group) video file
            ".mpeg",  # MPEG (Moving Picture Experts Group) video file
            ".rm",   # RealMedia file
            ".swf",  # Shockwave flash file
            ".vob",  # DVD Video Object
            ".webm",  # WebM video file
            ".wmv",  # Windows Media Video file
            ".gif",
        ]
        audio_formats = [
            ".mp3",  # MPEG Layer 3 Audio
            ".wav",  # Waveform Audio File Format
            ".aac",  # Advanced Audio Coding
            ".flac",  # Free Lossless Audio Codec
            ".ogg",  # Ogg Vorbis
            ".m4a",  # MPEG-4 Audio
            ".wma",  # Windows Media Audio
            ".mid",  # MIDI
            ".midi",  # Musical Instrument Digital Interface
            ".aiff",  # Audio Interchange File Format
            ".opus",  # Opus Audio Codec
            ".amr",  # Adaptive Multi-Rate Audio Codec
            ".au",   # Sun Microsystems and NeXT
            ".alac",  # Apple Lossless Audio Codec
            ".ape",  # Monkey's Audio
            ".dff",  # Direct Stream Digital Interchange File Format
            ".dsf",  # Direct Stream Digital
            ".mka",  # Matroska Audio
        ]
        executable_formats = [
            ".exe",  # Executable file for Windows
            ".bat",  # Batch file for Windows
            ".cmd",  # Command script for Windows
            ".com",  # Command file for DOS and Windows
            ".scr",  # Windows screensaver file
            ".msi",  # Microsoft Installer package for Windows
            ".msp",  # Microsoft Windows Installer patch
            ".dll",  # Dynamic Link Library for Windows
            ".apk",  # Android Package
            ".app",  # Application for macOS
            ".dmg",  # macOS Disk Image
            ".pkg",  # Installer package for macOS
            ".deb",  # Debian software package
            ".rpm",  # Red Hat Package Manager file
            ".sh",   # Shell script for Unix/Linux
            ".bin",  # Binary executable
            ".jar",  # Java Archive (executable)
            # Python script (executable in contexts with Python installed)
            ".py",
            ".pl",   # Perl script
            # PHP script (executable on a server or with a PHP interpreter)
            ".php",
            ".rb",   # Ruby script
            ".swift",  # Swift script
        ]
        document_formats = [
                ".doc",   # Microsoft Word Document
                ".docx",  # Microsoft Word Open XML Document
                ".html",  # Hypertext Markup Language
                ".htm",   # HTML (alternative extension)
                ".odt",   # OpenDocument Text Document
                ".pdf",   # Portable Document Format
                ".xls",   # Microsoft Excel Spreadsheet
                ".xlsx",  # Microsoft Excel Open XML Spreadsheet
                ".ods",   # OpenDocument Spreadsheet
                ".ppt",   # Microsoft PowerPoint Presentation
                ".pptx",  # Microsoft PowerPoint Open XML Presentation
                ".txt",   # Plain Text Document
            ]        
        compressed_formats = [".7z", ".zip", ".rar"]
        custom_formats = []

        self.extension(self.default_config_data, "Images", image_formats)
        self.extension(self.default_config_data, "Videos", video_formats)
        self.extension(self.default_config_data, "Audios", audio_formats)
        self.extension(self.default_config_data, "Executables", executable_formats)
        self.extension(self.default_config_data, "Documents", document_formats)
        self.extension(self.default_config_data, "Custom", custom_formats)
        self.extension(self.default_config_data, "Compressed", compressed_formats)

        # Add the workspaces
        downloads_path = pathlib.Path(pathlib.Path.home() / "Downloads")
        self.workspace(self.default_config_data, downloads_path, "Downloaded")

    @staticmethod
    def _user_config_path():
        """
        Returns the Path to the user config file
        """
        return pathlib.Path(ConfigManager._project_path() / ConfigManager.DATA_DIRECTORY / ConfigManager.USER_CONFIG_PATH)
    
    @staticmethod
    def _project_path() -> pathlib.Path:
        """
        Returns the path of the project
        """
        current_file_path = pathlib.Path(__file__)
        for parent in current_file_path.parents:
            if parent.name == constants.PROJECT_NAME:
                return parent
        raise ValueError(
            "Project path not found. Check the project folder name.")
    
    def _create_file(self, folder_directory, file_name):
        # # Creating the folder and the file paths
        project_path = self._project_path()
        folder_path = project_path / folder_directory
        file_path = pathlib.Path(
            folder_path) / file_name

        # Creating the folder and then the file in it
        folder_path.mkdir(exist_ok=True)
        file_path.touch(exist_ok=True)

        return file_path
