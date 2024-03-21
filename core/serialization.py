import sys
import pickle
import pathlib

import core.constants as constants


class Serializer():
    # The supported file extensions
    default_config = {
        "extensions": {

            "image": [
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
            ],

            "video": [
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
            ],

            "audio": [
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
            ],

            "executable": [
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
            ],

            "document": [
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
            ],
        },

        "workspaces": [
            pathlib.Path(pathlib.Path.home() / "Downloads")
        ]
    }

    DATA_FOLDER_NAME = "data"
    DEFAULT_CONFIG_FILE_NAME = "defaultconfig.pickle"
    # Getting the projects directory
    current_file_path = pathlib.Path(__file__)
    project_src_directory = current_file_path.parent
    project_directory = project_src_directory.parent

    # Creating a folder for the data files
    data_directory = project_directory / "data"
    pathlib.Path.mkdir(data_directory, exist_ok=True)

    # Creating the default config file
    default_config_file_path = data_directory / "defaultconfig.pickle"
    default_config_file_path.touch()

    def __init(self):
        self.create_default_config()

    def create_default_config(self) -> None:
        """
        Creates a binary file containing the default config
        """
        # Setting the data folder and the default config file names
        project_path = self._project_path()
        data_folder = project_path / self.DATA_FOLDER_NAME
        default_config_file = pathlib.Path(
            data_folder) / self.DEFAULT_CONFIG_FILE_NAME

        # Creating the folder and the file
        data_folder.mkdir(exist_ok=True)
        default_config_file.touch(exist_ok=True)

        # Comparing if the default config is not modified
        with open(default_config_file, "wb") as file:
            pickle.dump(self.default_config, file)

    def _project_path(self) -> pathlib.Path:
        current_file_path = pathlib.Path(__file__)
        for parent in current_file_path.parents:
            if parent.name == constants.PROJECT_NAME:
                return parent
        raise ValueError(
            "Project path not found. Check the project folder name.")

    def serialize(self, obj, path) -> None:
        try:
            with open(path, "wb") as pickle_file:
                pickle.dump(obj, pickle_file)
        except Exception as e:
            raise FileNotFoundError(f"{path.as_posix()} doesn't exists")

    def deserialize(self, path) -> object:
        try:
            with open(path, "rb"):
                return pickle.load(path)
        except:
            raise FileNotFoundError(f"{path.as_posix()} doesn't exists")
