import pickle


""" Brings methods for Serializing and deserializing data """

def serialize(obj, path) -> None:
    try:
        with open(path, "wb") as pickle_file:
            pickle.dump(obj, pickle_file)
    except Exception as e:
        raise FileNotFoundError(f"{path.as_posix()} doesn't exists")

def deserialize(path) -> object:
    try:
        with open(path, "rb") as file_path:
            return pickle.load(file_path)
    except:
        raise FileNotFoundError(f"{path.as_posix()} doesn't exists")
