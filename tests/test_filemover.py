import sys
sys.path.append("F:/DATOS/Documents/Projects/Python Projects/FilesOrganizer")

import unittest

from src.core.filemover import FileMover
from src.core.foldercontentgiver import FolderContentGiver
from src.constants import DOWNLOADS_FOLDER_PATH
from src.constants import DirectoryType

class TestFileMover(unittest.TestCase):
    def test_move_all_files(self):
        giver = FolderContentGiver(DOWNLOADS_FOLDER_PATH)
        files_absolute_path = giver.files(format=DirectoryType.ABSOLUTE_PATH)

        for file_abs_path in files_absolute_path:
            self.assertIsInstance(file_abs_path, str)

        mover = FileMover(DOWNLOADS_FOLDER_PATH / "Images")
        mover.move(files_absolute_path)

        self.assertTrue(len(giver.files()) == 0)
        
if __name__ == "__main__":
    unittest.main()