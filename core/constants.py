from enum import Enum
from enum import auto

PROJECT_NAME = "FilesOrganizer"

class DirectoryType(Enum):
    """
    This enum is used solely in the folder_content_giver.py
    """
    PATH_OBJECT = auto()
    ABSOLUTE_PATH = auto()
    NAME_ONLY = auto()