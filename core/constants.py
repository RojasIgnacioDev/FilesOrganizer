import pathlib
from enum import Enum
from enum import auto

PROJECT_NAME = "FilesOrganizer"
PROJECT_PATH = pathlib.Path(__file__).parent.parent

class DirectoryType(Enum):
    """
    This enum is used solely in the folder_content_giver.py
    """
    PATH_OBJECT = auto()
    ABSOLUTE_PATH = auto()
    NAME_ONLY = auto()

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
compressed_formats = [
    ".7z",
    ".zip", 
    ".rar"
]
