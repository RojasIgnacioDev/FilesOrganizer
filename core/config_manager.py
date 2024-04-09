import sys
sys.path.append("F:/DATOS/Documents/Projects/Python Projects/FilesOrganizer")

import pathlib

from core.folder_content_giver import FolderContentGiver
import core.constants as constants

class ConfigManager():
    default_config_data = None

    # Constructor
    # def __init__(self) -> None:
    #     """
    #     Creates the default config data at the instantiation of the class object
    #     """
    #     self.default_config_data = {"extensions": [], "workspaces": []}
    #     # Add the extensions
        
    #     self.extension(self.default_config_data, "Images", image_formats)
    #     self.extension(self.default_config_data, "Videos", video_formats)
    #     self.extension(self.default_config_data, "Audios", audio_formats)
    #     self.extension(self.default_config_data, "Executables", executable_formats)
    #     self.extension(self.default_config_data, "Documents", document_formats)
    #     self.extension(self.default_config_data, "Compressed", compressed_formats)

    #     # Add the workspaces
    #     downloads_path = pathlib.Path(pathlib.Path.home() / "Downloads")
    #     self.workspace(self.default_config_data, downloads_path, "Downloaded")

    @staticmethod
    def print_workspaces(config):
        workspaces :list= config["workspaces"]
        print("\n\n\nWorkspaces")
        for workspace in workspaces:
            name = workspace["name"]
            path = workspace["path"]
            prefix = workspace["prefix"]
            print(f"■\t{name} in {path}. Prefix = '{prefix}'")

    @staticmethod
    def workspaces(config):
        """
        Returns the workspaces of the given config
        """
        workspaces = config["workspaces"]
        return workspaces

    def extensions(self, config):
        """
        Returns the extensions of the given config
        """
        extensions = config["extensions"]
        return extensions
    
    @staticmethod
    def workspace(config, path, prefix):
        """
        Creates a new workspace in the config obj
        """
        if not isinstance(path, pathlib.Path):
            path = pathlib.Path(path)
        workspaces = config["workspaces"]
        workspaces.append({"name": path.name, "path": path, "prefix": prefix})
        
    @staticmethod
    def extension(config, category, formats: list):
        """
        Creates a new extension in the config obj
        """
        extensions = config["extensions"]
        extensions.append({"category": category, "formats": formats})

    @staticmethod
    def default_config():
        return ConfigManager.default_config_data

    def is_workspace_organized(self, config, workspace_name):
        workspace = [ws for ws in config["workspaces"] if ws["name"] == workspace_name].pop()
        workspace_path = workspace["path"]
        workspace_files = FolderContentGiver(workspace_path).files()
        return len(workspace_files) == 0

    @staticmethod
    def _project_path() -> pathlib.Path:
        """
        Returns the path of the project
        """
        current_file_path = pathlib.Path(__file__)
        for parent in current_file_path.parents:
            if parent.name == constants.PROJECT_NAME:
                return parent
        raise ValueError(
            "Project path not found. Check the project folder name.")
    
    def _create_file(self, folder_directory, file_name):
        # # Creating the folder and the file paths
        project_path = self._project_path()
        folder_path = project_path / folder_directory
        file_path = pathlib.Path(
            folder_path) / file_name

        # Creating the folder and then the file in it
        folder_path.mkdir(exist_ok=True)
        file_path.touch(exist_ok=True)

        return file_path
