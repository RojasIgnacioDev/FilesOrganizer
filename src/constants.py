import pathlib
from enum import Enum
from enum import auto


class DirectoryType(Enum):
    PATH_OBJECT = auto()
    ABSOLUTE_PATH = auto()
    NAME_ONLY = auto()
