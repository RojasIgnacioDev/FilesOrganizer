from os import stat
from stat import FILE_ATTRIBUTE_HIDDEN as HIDDEN_FILE
from stat import FILE_ATTRIBUTE_SYSTEM as SYSTEM_FILE
from stat import FILE_ATTRIBUTE_READONLY as READONLY_FILE
from pathlib import Path
from shutil import move

class FolderContentGiver:
    banned_attributes = [
        HIDDEN_FILE,
        SYSTEM_FILE,
        READONLY_FILE,
    ]

    def __init__(self, path):
        self.path = path
        self.directories = list[Path]

    def __call__(self):
        directories = self._get_secure_directories(self.path)
        return directories

    def _get_raw_directories(self, path: Path):
        assert path.is_dir(), "The path provided is not a folder"

        # Get the directories of the Downloads folder
        raw_directories = [dir for dir in path.iterdir()]
        return raw_directories

    
    def _get_secure_directories(self, path : Path):
        unsecure_directories = self._get_raw_directories(path)
        secure_directories = []

        for directory in unsecure_directories:
            if not self._has_banned_attributes(directory):
                secure_directories.append(directory)
        
        return secure_directories
    
    def _has_banned_attributes(self, directory: Path):
        attributes = stat(directory).st_file_attributes
        # Check against all banned attributes
        for banned_attribute in self.banned_attributes:
            if attributes & banned_attribute:
                return True
        return False
    
downloads_folder = Path(Path.home() / "Downloads")
content = FolderContentGiver(downloads_folder)()
pass