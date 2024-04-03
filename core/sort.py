import pathlib
import os

from core.folder_content_giver import FolderContentGiver
from core.file_mover import FileMover
import core.constants as constants

def sort(config):
    extensions = config["extensions"]
    workspaces = config["workspaces"]

    for workspace in workspaces:
        # Gets the files in the workspace
        giver = FolderContentGiver(workspace["path"])
        unsorted_files = giver.files()
        
        for extension in extensions:
            # extension type are image, document, video, etc
            for format in extension["formats"]:
                # format are .png, .jpg, .exe, etc

                # Gets the files with an specific format
                files = [file for file in unsorted_files if is_file_type(file, format)]

                if len(files) > 0:
                    # creates a folder using the extension workspace prefix and the extension category
                    prefix = workspace["prefix"]
                    category = extension["category"]
                    category_folder = pathlib.Path(workspace["path"]) / f"{prefix} {category}"
                    category_folder.mkdir(exist_ok=True)

                    try:
                        FileMover.move(category_folder, files)
                    except(FileMover.FileAlreadyExistsError):
                        FileMover.move_with_rename(category_folder, files)
                    
def is_file_type(file_path, extension_type):
    file : str = file_path.name
    # file_extension = "." + file.split(".", -1)[-1]
    filename, extension = os.path.splitext(file)
    extension = extension.lower()
    return extension == extension_type
