from enum import Enum
from enum import auto

PROJECT_NAME = "FilesOrganizer"

class DirectoryType(Enum):
    PATH_OBJECT = auto()
    ABSOLUTE_PATH = auto()
    NAME_ONLY = auto()