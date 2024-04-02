import pathlib
import shutil

class FileMover:
    """
    Changes the location of directories
    """
    
    @staticmethod
    def move(destination_folder: pathlib.Path, directories: list):
        """
        Takes a list of directories and moves them into the destination folder
        """
        if not destination_folder.is_dir():
            raise FileMover.FolderPathError()
        
        for directory in directories:
            shutil.move(directory, destination_folder)

    class FolderPathError(Exception):
        def __init__(self):
            self.message = "Expected folder path"
            super().__init__(self.message)