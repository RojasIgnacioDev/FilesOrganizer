import sys
import pickle
import pathlib

import core.constants as constants


class Serializer():
    DATA_DIRECTORY = pathlib.Path("data")
    DEFAULT_CONFIG_FILE_NAME = pathlib.Path("defaultconfig.pickle")
    USER_CONFIG_FILE_NAME = pathlib.Path("userconfig.pickle")
    # The supported file extensions

    # The supported file extensions
    default_config_data = {
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

    def create_default_config(self) -> None:
        """
        Creates a binary file containing the default config
        """
        # Setting the data folder and the default config file names
        default_config_file = self._create_file(
            self.DATA_DIRECTORY, self.DEFAULT_CONFIG_FILE_NAME)

        # Comparing if the default config is not modified
        self._serialize(self.default_config_data, default_config_file)

    def default_config(self) -> object:
        return self._deserialize(self._default_config_path())

    def create_user_config(self):
        self._create_file(self.DATA_DIRECTORY, self.USER_CONFIG_FILE_NAME)

    def _default_config_path(self):
        return pathlib.Path(self._project_path() / self.DATA_DIRECTORY / self.DEFAULT_CONFIG_FILE_NAME)

    def _create_file(self, folder_directory, file_name):
        # # Creating the folder and the file paths
        project_path = self._project_path()
        folder_path = project_path / folder_directory
        file_path = pathlib.Path(
            folder_path) / file_name

        # Creating the folder and the file themselves
        folder_path.mkdir(exist_ok=True)
        file_path.touch(exist_ok=True)

        return file_path

    def _project_path(self) -> pathlib.Path:
        current_file_path = pathlib.Path(__file__)
        for parent in current_file_path.parents:
            if parent.name == constants.PROJECT_NAME:
                return parent
        raise ValueError(
            "Project path not found. Check the project folder name.")

    def _serialize(self, obj, path) -> None:
        try:
            with open(path, "wb") as pickle_file:
                pickle.dump(obj, pickle_file)
        except Exception as e:
            raise FileNotFoundError(f"{path.as_posix()} doesn't exists")

    def _deserialize(self, path) -> object:
        try:
            with open(path, "rb"):
                return pickle.load(path)
        except:
            raise FileNotFoundError(f"{path.as_posix()} doesn't exists")

Serializer()