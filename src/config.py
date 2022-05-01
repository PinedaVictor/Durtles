# DRT configuration


import os

# TODO: Imlement drt config class.
#       should handle all env varibles such as path, editing path, user input, etc...


class DrtConfig:

    __CURRENT_DIR = os.getcwd()
    __PARENT_PATH = os.path.dirname(__CURRENT_DIR)
    __EDITING_DIR = "{0}/Edit".format(__PARENT_PATH)
    __MISSPELLED_DIR = "{0}/Misspelled".format(__PARENT_PATH)

    def __init__(self) -> None:
        pass

    # This is default in nature
    # May not require setter functions
    def get_current_dir(self) -> str:
        return self.__CURRENT_DIR

    def get_parent_path(self) -> str:
        return self.__PARENT_PATH

    def get_editing_dir(self) -> str:
        return self.__EDITING_DIR

    def set_editing_dir(self, editingDir) -> None:
        print("Setting the editing path")
        # TODO: Verify editing dir is a valid directory
        # FIXME: If path within parent path, handle folder name or create path.
        if os.path.isdir(editingDir):
            self.__EDITING_DIR = editingDir

    def get_missppelled_dir(self) -> str:
        return self.__MISSPELLED_DIR
