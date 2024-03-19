from os import stat
from stat import (
    FILE_ATTRIBUTE_HIDDEN as HIDDEN_FILE,
    FILE_ATTRIBUTE_SYSTEM as SYSTEM_FILE,
    FILE_ATTRIBUTE_READONLY as READONLY_FILE,
)
from pathlib import Path
from enum import Enum
from enum import auto

class DirectoryType(Enum):
    PATH_OBJECT = auto()
    ABSOLUTE_PATH = auto()
    NAME_ONLY = auto()

class FolderContentGiver:
    banned_file_attributes = [
        HIDDEN_FILE,
        SYSTEM_FILE,
        READONLY_FILE,
    ]

    def __init__(self, path):
        self.path = path
        self.directories = list[Path]

    def files_and_folders(self, format=DirectoryType.PATH_OBJECT):
        """
        Returns a list with all the files and the folders in the specified path at the class instantiation
        """
        directories = self._secure_directories(self.path)
        files_and_folders = self._format_directories(directories, format)
        return directories

    def files(self, format=DirectoryType.PATH_OBJECT):
        """
        Returns a list with all the files, excluding the folders, in the specified path at the class instantiation
        """
        directories = self._secure_directories(self.path)
        files = [dir for dir in directories if dir.is_file()]
        files = self._format_directories(files, format)
        return files

    def folders(self, format=DirectoryType.PATH_OBJECT):
        """
        Returns a list with all the folders, excluding the files, in the specified path at the class instantiation
        """
        directories = self._secure_directories(self.path)
        folders = [dir for dir in directories if dir.is_dir()]
        folders = self._format_directories(folders, format)
        return folders

    def _format_directories(self, directories, format : DirectoryType):
        match format:
            case DirectoryType.PATH_OBJECT:
                return [dir for dir in directories]
            case DirectoryType.ABSOLUTE_PATH:
                return self._directories_absolute_path(directories)
            case DirectoryType.NAME_ONLY:
                return self._directories_name(directories)

    def _directories_name(self, directories):
        directories_names = [dir.name for dir in directories]
        return directories_names

    def _directories_absolute_path(self, directories):
        directories_names = [dir.as_posix() for dir in directories]
        return directories_names

    def _get_raw_directories(self, path: Path):
        assert path.is_dir(), "The path provided is not a folder"

        # Get the directories of the Downloads folder
        raw_directories = [dir for dir in path.iterdir()]
        return raw_directories

    def _secure_directories(self, path : Path):
        unsecure_directories = self._get_raw_directories(path)
        secure_directories = []

        for directory in unsecure_directories:
            if not self._has_banned_file_attributes(directory):
                secure_directories.append(directory)
        
        return secure_directories
    
    def _has_banned_file_attributes(self, directory: Path):
        attributes = stat(directory).st_file_attributes
        # Check against all banned attributes
        for banned_attribute in self.banned_file_attributes:
            if attributes & banned_attribute:
                return True
        return False