import pathlib
import importlib


from foldercontentgiver import FolderContentGiver
from filemover import FileMover
from sortconfigmanager import SortConfigManager
import constants as constants


def sort(config):
    extensions = config["extensions"]
    workspaces = config["workspaces"]

    for workspace in workspaces:
        # Gets the files in the workspace
        giver = FolderContentGiver(workspace)
        unsorted_files = giver.files()
        
        for extension_type in extensions:
            # extension type are image, document, video, etc
            for extension in extensions[extension_type]:
                # extension are .png, .jpg, .exe, etc

                files = [file for file in unsorted_files if is_file_type(file, extension)]
                if len(files) > 0:
                    pass
    pass    

def is_file_type(file_path, extension_type):
    file : str = file_path.name
    file_extension = "." + file.split(".", -1)[1]
    return file_extension == extension_type

sort(SortConfigManger.default_config)