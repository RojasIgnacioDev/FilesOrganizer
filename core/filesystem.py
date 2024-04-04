import sys
sys.path.append("F:/DATOS/Documents/Projects/Python Projects/FilesOrganizer")
import pathlib
import os
import constants

# class Workspace:

    
#     workspace_folders = {}

#     def __init__(self):
#         pass

#     def create_folder(self, name="Unnamed", extension_list=[]):
#         """
#         Creates a folder that will only store files that have their extension included in the extension format list passed as argument
#         """
#         new_folder = self.Folder(name, extension_list)
#         self.workspace_folders[name] = new_folder

#     def get_folder(self, key):
#         return self.workspace_folders[key]

#     def _add_folder_to_workspace(self, folder_object):
#         """
        
#         """
#         raise NotImplementedError()



class Configuration:
    workspace_folders = {}
    
    def __init__(self):
        self._new_folder("Images", constants.image_formats)
        self._new_folder("Videos", constants.video_formats)
        self._new_folder("Audios", constants.audio_formats)
        self._new_folder("Executables", constants.executable_formats)
        self._new_folder("Documents", constants.document_formats)
        self._new_folder("Compressed", constants.compressed_formats)

    def _new_folder(self, category_name, extension_list):
        """
        Adds a folder that will store files including one of the extensions passed as a list
        """
        self.workspace_folders[category_name] = Folder(category_name, extension_list)
    
# TODO: finish the folder class so it can store all the files stored in int
# TODO: make a method that returns all its files stored in
# TODO: make the folder moves its files that do not has one of the extensions to the parent dir
class Folder:
    name = None
    path : pathlib.Path
    extensions: list
    files = []

    def __init__(self, name: str, extensions: list):
        self.name = name
        self.path = pathlib.Path(constants.DOWNLOADS_PATH / name)
        self.path.mkdir(exist_ok=True)
        self.extensions = extensions
        self.files = [path for path in self.path.iterdir() if path.is_file()]
        self.remove_stranger_files()

    def remove_stranger_files(self):
        """
        Removes files that do not fulfill having one of the extensions specified in the instantiation of the class
        """
        
        all_files = [dir for dir in self.path.iterdir() if dir.is_file()]
        odd_files = [filename for filename in all_files if self._is_file_stranger(filename)]

    def _is_file_stranger(self, filename: pathlib.Path):
        for extension in self.extensions:
            file_extension = os.path.splitext(filename)
            pass
        return True

class File:
    def __init__(self, path: pathlib.Path):
        assert path.is_file(), "Expected a file path"
        self.path = path
        self.name = self.path.name
        self.root = self.path.stem
        self.extension = self.path.suffix
        
###
# For debugging
###
Configuration()
pass