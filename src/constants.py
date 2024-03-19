import pathlib
from enum import Enum
from enum import auto

DOWNLOADS_FOLDER_PATH = pathlib.Path(pathlib.Path.home() / "Downloads")

class DirectoryType(Enum):
    PATH_OBJECT = auto()
    ABSOLUTE_PATH = auto()
    NAME_ONLY = auto()