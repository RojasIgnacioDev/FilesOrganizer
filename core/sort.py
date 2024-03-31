import pathlib
import importlib


from foldercontentgiver import FolderContentGiver
from filemover import FileMover
import constants as constants


def sort(config):
    extensions = config["extensions"]
    workspaces = config["workspaces"]

    for workspace in workspaces:
        # Gets the files in the workspace
        giver = FolderContentGiver(workspace)
        unsorted_files = giver.files()
        
        for extension in extensions:
            # extension type are image, document, video, etc
            for format in extensions[extension]:
                # format are .png, .jpg, .exe, etc

                # Gets the files with an specific format
                files = [file for file in unsorted_files if is_file_type(file, format)]

                if len(files) > 0:
                    # move every file into its corresponding folder
                    for file in files:
                        

                    pass
    pass    

def is_file_type(file_path, extension_type):
    file : str = file_path.name
    file_extension = "." + file.split(".", -1)[1]
    return file_extension == extension_type
