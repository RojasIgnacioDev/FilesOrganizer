import pathlib
import shutil
import os

class FileMover:
    """
    Changes the location of directories
    """
    
    @staticmethod
    def move_with_rename(destination_folder: pathlib.Path, directories: list):
        """
        Takes a list of directories and moves them into the destination folder, renaming the files if there is already identical ones
        """
        for file_path in directories:
            destination_path = destination_folder / file_path.name
            if destination_path.exists():
                filename, extension = os.path.splitext(file_path.name)
                counter = 1
                while destination_path.exists():
                    new_filename = f"{filename}_{counter}{extension}"
                    destination_path = destination_folder / new_filename
                    counter += 1

            shutil.move(file_path, destination_path)
    
    
    @staticmethod
    def move_with_overwrite(destination_folder: pathlib.Path, directories: list):
        """Moves files into the new destination_folder path, overwriting existing identical files"""
        for file_path in directories:
            try:
                shutil.move(file_path, destination_folder)
            except(shutil.Error):
                os.remove(file_path)
                shutil.move(file_path, destination_folder)

    @staticmethod
    def move(destination_folder: pathlib.Path, directories: list):
        """
        Takes a list of directories and moves them into the destination folder
        """
        if not destination_folder.is_dir():
            raise FileMover.FolderPathError()
        
        for directory in directories:
            try:
                shutil.move(directory, destination_folder)
            except(shutil.Error):
                raise FileMover.FileAlreadyExistsError()

    class FileAlreadyExistsError(Exception):
        def __init__(self):
            super().__init__("File already exists")

    class FolderPathError(Exception):
        def __init__(self):
            super().__init__("Expected folder path")