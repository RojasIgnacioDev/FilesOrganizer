import constants
import os
import pathlib
import sys
sys.path.append("F:/DATOS/Documents/Projects/Python Projects/FilesOrganizer")

# TODO: finish the folder class so it can store all the files stored in it
# TODO: make a method that returns all its files stored in
# TODO: make the folder moves its files that do not has one of the extensions to the parent dir

class Workspace:
    def __init__(self) -> None:
        raise NotImplementedError()

class Folder:
    """Represents a directory as a folder"""
    path: pathlib.Path
    name = None

    def __init__(self, path, name: str):
        # self.path = pathlib.Path(constants.DOWNLOADS_PATH / name)
        self.path = path / name
        self.path.mkdir(exist_ok=True)
        self.name = self.path.name

    def files(self) -> list:
        """Returns a list of files"""
        files_object_list = [
            File(file_path) for file_path in self.path.iterdir() if file_path.is_file()]
        return files_object_list

class SpecialFolder(Folder):
    """A type of folder that only holds files with specific extensions"""

    extensions: list

    def __init__(self, path, name: str, extensions: list):
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

class File:
    """Represents a file"""

    def __init__(self, path: pathlib.Path):
        assert path.is_file(), "Expected a file path"
        self.path = path
        self.name = self.path.name
        self.root = self.path.stem
        self.extension = self.path.suffix

# For debugging
Folder(constants.DOWNLOADS_PATH, "Audios")
pass
