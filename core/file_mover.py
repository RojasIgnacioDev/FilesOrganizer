import pathlib
import shutil

class FileMover:
    """
    Changes the location of directories
    """

    @staticmethod
    def move_directories(destination_folder: pathlib.Path, directories: list):
        if destination_folder:
            raise FileMover.FolderPathError()
        
        for directory in directories:
            shutil.move(directory, destination_folder)

    class FolderPathError(Exception):
        def __init__(self):
            self.message = "Expected folder path"
            super().__init__(self.message)