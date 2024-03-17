from os import stat
from stat import FILE_ATTRIBUTE_HIDDEN as HIDDEN_FILE
from stat import FILE_ATTRIBUTE_SYSTEM as SYSTEM_FILE
from stat import FILE_ATTRIBUTE_READONLY as READONLY_FILE
from pathlib import Path
from shutil import move

# The supported file extensions 
image_extensions = [
    ".jpg",  # Joint Photographic Experts Group
    ".png",  # Portable Network Graphics
    "jpeg",  # JPEG format (alternative extension)
    ".webp", # Modern format for web images
    ".tiff", # Tagged Image File Format
    ".psd",  # Photoshop Document
    ".raw",  # High-quality image format from digital cameras
    ".bmp",  # Bitmap Image File
    ".heif", # High Efficiency Image File Format
    ".indd", # Adobe InDesign Document
    ".tif",  # TIFF (alternative extension)
    ".svg",  # Scalable Vector Graphics
    ".ai",   # Adobe Illustrator Artwork image
    ".eps",  # Encapsulated PostScript
]

video_extensions = [
    ".3g2",  # 3GPP2 multimedia file
    ".3gp",  # 3GPP multimedia file
    ".avi",  # AVI (Audio Video Interleave) file
    ".flv",  # Adobe Flash file
    ".h264", # H.264 video file
    ".m4v",  # Apple MP4 video file
    ".mkv",  # Matroska Multimedia Container
    ".mov",  # Apple QuickTime movie
    ".mp4",  # MPEG4 video file
    ".mpg",  # MPEG (Moving Picture Experts Group) video file
    ".mpeg", # MPEG (Moving Picture Experts Group) video file
    ".rm",   # RealMedia file
    ".swf",  # Shockwave flash file
    ".vob",  # DVD Video Object
    ".webm", # WebM video file
    ".wmv",  # Windows Media Video file
    ".gif",
]

audio_extensions = [
    ".mp3",  # MPEG Layer 3 Audio
    ".wav",  # Waveform Audio File Format
    ".aac",  # Advanced Audio Coding
    ".flac", # Free Lossless Audio Codec
    ".ogg",  # Ogg Vorbis
    ".m4a",  # MPEG-4 Audio
    ".wma",  # Windows Media Audio
    ".mid",  # MIDI
    ".midi", # Musical Instrument Digital Interface
    ".aiff", # Audio Interchange File Format
    ".opus", # Opus Audio Codec
    ".amr",  # Adaptive Multi-Rate Audio Codec
    ".au",   # Sun Microsystems and NeXT
    ".alac", # Apple Lossless Audio Codec
    ".ape",  # Monkey's Audio
    ".dff",  # Direct Stream Digital Interchange File Format
    ".dsf",  # Direct Stream Digital
    ".mka",  # Matroska Audio
]

executable_extensions = [
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
    ".py",   # Python script (executable in contexts with Python installed)
    ".pl",   # Perl script
    ".php",  # PHP script (executable on a server or with a PHP interpreter)
    ".rb",   # Ruby script
    ".swift",# Swift script
]

document_extensions = [
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

# TODO Native and custom file extension lists 

# The folder names to store the files
images_folder = "Downloaded Images"
videos_folder = "Downloaded Videos"
audio_folder = "Downloaded Audio"
executables_folder = "Downloaded Executables"
documents_folder = "Downloaded Documents"


# TODO Create a dictionary with all the targeted folder to sort its files

# TODO Create a dictionary that contains the folder names and the the files with the specified extensions 


# The user's Downloads folder
downloads_folder = Path(Path.home() / "Downloads")

def get_secure_directories(unsecure_directories : list[Path]):
    """
    Returns a list of secure directories that shouldn't cause problems if these are modified/deleted
    """

    secure_directories = []

    def has_attribute(dir, attribute):
        return bool(stat(dir).st_file_attributes & attribute)

    # Checks for the directories
    for directory in unsecure_directories:
        # Checks if the directory has a hidden attribute
        if has_attribute(directory, HIDDEN_FILE):
            continue

        # Checks if the directory has a system attribute
        if has_attribute(directory, SYSTEM_FILE):
            continue

        # Checks if the directory has a read-only attribute
        if has_attribute(directory, READONLY_FILE):
            continue
        
        # Adds the directory as a secure directory
        secure_directories.append(directory)
    
    return secure_directories

def get_specified_files(directories, extensions):
    """
    Returns a list with the files that are not the ones passed in the parameter
    """

    specified_files = []

    for directory in directories:
        # Checks if the directory is not a folder
        if not directory.is_dir():
            # Gets the file extension 
            file_path = directory.as_posix()
            _, separator, extension = file_path.rpartition(".")
            file_extension = separator + extension
            
            # Checks if extension matches with the extensions given
            if file_extension in extensions:
                file_directory = directory
                specified_files.append(file_directory)
    
    return specified_files

def get_directories():
    """
    Returns a list with the directories of the Downloads folder. Ignores special directories.
    """

    # Get the directories of the Downloads folder
    raw_directories = [dir for dir in downloads_folder.iterdir()]

    # Filters the insecure directories
    secure_directories = get_secure_directories(raw_directories)

    return secure_directories

def sort_files(destination_folder, extensions):
    """
    Creates a folder with the specified name and moves in it the files with the specified extensions
    """
    
    # The path to the destination folder
    dest_folder = Path(downloads_folder / destination_folder)

    # Creates a destination folder if it doesn't exists
    dest_folder.mkdir(parents=True, exist_ok=True)
    
    # Obtains the content of the Downloads folder
    directories = get_directories()
    
    # Extracts the files with the specified extensions
    specified_files = get_specified_files(directories, extensions)

    # Moves the files to the destination folder
    for file in specified_files:
        move(file, dest_folder)
