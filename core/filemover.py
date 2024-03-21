import pathlib
import shutil

class FileMover():
    """

    """
    def __init__(self, path):
        folder_path = pathlib.Path(path)

        assert folder_path.is_dir(), "Expected folder path. Given file path"
        self.destination_folder = path
        pass

    def change_destination_folder(self, folder_path):
        directory = pathlib.Path(folder_path)
        
        if not directory.is_dir(): 
            raise self.FolderPathError()
        
        self.destination_folder = directory

    def move(self, directories):
        for directory in directories:
            shutil.move(directory, self.destination_folder)

    class FolderPathError(Exception):
        def __init__(self):
            self.message = "Expected folder path"
            super().__init__(self.message)