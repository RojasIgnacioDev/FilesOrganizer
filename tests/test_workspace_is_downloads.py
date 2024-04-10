import sys
sys.path.append("F:/DATOS/Documents/Projects/Python Projects/FilesOrganizer")
from core import filesystem
from core import constants

def test_workspace_folder_is_in_downloads_path():
    workspace = filesystem.DownloadsWorkspace()
    workspace_path = workspace.folder.path
    assert workspace_path == constants.DOWNLOADS_PATH
