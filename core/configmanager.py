import sys
sys.path.append("F:/DATOS/Documents/Projects/Python Projects/FilesOrganizer")
import pathlib

from core.serialization import serialize
import core.constants as constants

class ConfigManager():
    # Folder where the user config will be stored 
    DATA_DIRECTORY = pathlib.Path("data")
    # 
    USER_CONFIG_PATH = pathlib.Path("userconfig.pickle")

    default_config_data = None

    def __init__(self) -> None:
        self._create_default_config()

    def workspace(self, config, path: pathlib.Path, prefix):
        """
        Creates a new workspace in the config obj
        """
        workspaces = config["workspaces"]
        workspaces.append({"path": path, "prefix": prefix})

    def extension(self, config, category, formats: list):
        """
        Creates a new extension in the config obj
        """
        extensions = config["extensions"]
        extensions.append({"category": category, "formats": formats})

    def default_data(self):
        return self.default_config_data

    # not used
    def reset_user_config(self):
        """
        Overwrites the current user config with the default data
        """
        user_config_path = self._user_config_path()
        serialize(self.default_config_data, user_config_path)
        pass

    # not used
    def user_config_exists(self):
        return self._user_config_path().exists()

    # not used
    def folder(self, from_path: pathlib.Path, prefix_name, last_name):
        """
        Creates a folder from a specified path, making its name in base of the prefix and the last name
        """
        path = from_path / f"{prefix_name} {last_name}"
        path.mkdir(exist_ok=True)
        
    # not used
    def move_files_to_folder(self):

        raise NotImplementedError()

    # not used
    def move_files_to_subfolder(self):
        raise NotImplementedError()


    def _user_config_path(self):
        """
        Returns the Path to the user config file
        """
        return pathlib.Path(self._project_path() / self.DATA_DIRECTORY / self.USER_CONFIG_PATH)
    
    def _project_path(self) -> pathlib.Path:
        """
        Returns the path of the project
        """
        current_file_path = pathlib.Path(__file__)
        for parent in current_file_path.parents:
            if parent.name == constants.PROJECT_NAME:
                return parent
        raise ValueError(
            "Project path not found. Check the project folder name.")
    
    def create_user_config(self):
        self._create_file(self.DATA_DIRECTORY, self.USER_CONFIG_PATH)

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


