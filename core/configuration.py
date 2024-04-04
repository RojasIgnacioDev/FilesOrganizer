class Workspace:
    """
    Creates a Workpaces object that contains folders where the sorted files will be stored
    """
    
    workspace_folders = {}

    def __init__(self):
        pass

    def create_folder(self, name="Unnamed", extension_list=[]):
        """
        Creates a folder that will only store files that have their extension included in the extension format list passed as argument
        """
        new_folder = self.Folder(name, extension_list)
        self.workspace_folders[name] = new_folder

    def get_folder(self, key):
        return self.workspace_folders[key]

    def _add_folder_to_workspace(self, folder_object):
        """
        
        """
        raise NotImplementedError()

    class Folder:
        def __init__(self, name: str, extensions: list):
            pass

class Configuration:
    workspaces = Workspace()
    def __init__(self):
        pass

