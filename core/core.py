from os import stat
from stat import FILE_ATTRIBUTE_HIDDEN as HIDDEN_FILE
from stat import FILE_ATTRIBUTE_SYSTEM as SYSTEM_FILE
from stat import FILE_ATTRIBUTE_READONLY as READONLY_FILE
from pathlib import Path
from shutil import move


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
