from core import constants
import pathlib
import os
import sys
sys.path.append("F:/DATOS/Documents/Projects/Python Projects/FilesOrganizer")


# TODO: finish the folder class so it can store all the files stored in it
# TODO: make a method that returns all its files stored in
# TODO: make the folder moves its files that do not has one of the extensions to the parent dir

# region Workspace and DownloadsWorkspace classes

class Workspace:
    folders = {}

    def __init__(self, path: pathlib.Path) -> None:
        self.folder = Folder(path, path.name)

    def add_special_folder(self, folder_name, extensions):
        """Adds a new special folder in the workspace folder"""
        new_folder = SpecialFolder(self.folder.path, folder_name, extensions)
        self.folders[folder_name] = new_folder

    def directories(self):
        """Returns files and folders"""
        return [dir for dir in self.folder.directories()]


class DownloadsWorkspace(Workspace):
    """Creates a Workspace in the system Downloads folder"""

    def __init__(self, path=constants.DOWNLOADS_PATH) -> None:
        super().__init__(path)
        self.add_special_folder("Images", constants.image_formats)

    def get_extension_files(self, extensions_list):
        """Returns a list of File objects representing files that fulfill having a extension in the extensions_list"""

# endregion

# region Folder and SpecialFolder classes

class Folder:
    """Represents a directory as a folder"""
    path: pathlib.Path
    name = None

    def __init__(self, path: pathlib.Path, name: str):
        # self.path = pathlib.Path(constants.DOWNLOADS_PATH / name)
        
        if not path.name == name:
            self.path = path / name
        else:
            self.path = path
            
        self.path.mkdir(exist_ok=True)
        self.name = self.path.name

    def files(self) -> list:
        """Returns a list of File objects"""
        file_objects_list = [
            File(file_path) for file_path in self.path.iterdir() if file_path.is_file()]
        return file_objects_list

    def folders(self):
        """Returns a list of Folder objects"""
        folder_path_list = [
            folder_path for folder_path in self.path.iterdir() if folder_path.is_dir()]

        folder_objects_list = []
        for path in folder_path_list:
            folder_objects_list.append(Folder(path, path.name))

        return folder_objects_list

    def directories(self):
        """Returns a list of folders and files"""
        path_list = [path for path in self.path.iterdir()]
        return path_list


class SpecialFolder(Folder):
    """A type of folder that only holds files with specific extensions"""

    extensions: list

    def __init__(self, path: pathlib.Path, name: str, extensions: list):
        super().__init__(path, name)
        self.extensions = extensions
        self.remove_stranger_files()

    def remove_stranger_files(self):
        """Returns a list of files that do not fulfill having one of the extensions specified in the instantiation of the class"""
        all_files = self.files()
        odd_files = [
            file for file in all_files if self._is_file_stranger(file)]
        # TODO: finish the functionality of the method

    def _is_file_stranger(self, file):
        file_extension = file.extension
        for extension in self.extensions:

            if not file_extension == extension:
                return True

        return False

# endregion

class File:
    """Represents a file"""

    def __init__(self, path: pathlib.Path):
        assert path.is_file(), "Expected a file path"
        self.path = path
        self.name = self.path.name
        self.root = self.path.stem
        self.extension = self.path.suffix

# For debugging
# Folder(constants.DOWNLOADS_PATH, "Audios")

