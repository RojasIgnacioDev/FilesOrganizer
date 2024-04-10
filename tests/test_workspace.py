import sys
sys.path.append("F:/DATOS/Documents/Projects/Python Projects/FilesOrganizer")

from core import filesystem

def test_get_directories():
    workspace = filesystem.DownloadsWorkspace()
    assert isinstance(workspace, filesystem.DownloadsWorkspace)

