# DRT configuration

import os

import utils.colors as colors

# TODO: Imlement drt config class.
#       should handle all env varibles such as path, editing path, user input, etc...

Colors = colors.Colors()


class DrtConfig:

    __CURRENT_DIR = os.getcwd()
    __PARENT_PATH = os.path.dirname(__CURRENT_DIR)
    # __EDITING_DIR = ""
    __MISSPELLED_DIR = "{0}/Misspelled".format(__PARENT_PATH)

    def __init__(self, edit_directory: str) -> None:
        self.__EDITING_DIR = edit_directory
        # __EDITING_DIR = "{0}/Edit".format(__PARENT_PATH)
        # __MISSPELLED_DIR = "{0}/Misspelled".format(__PARENT_PATH)

        # pass

    # This is default in nature
    # May not require setter functions
    def get_current_dir(self) -> str:
        return self.__CURRENT_DIR

    def get_parent_path(self) -> str:
        return self.__PARENT_PATH

    def get_editing_dir(self) -> str:
        return self.__EDITING_DIR

    def set_editing_dir(self) -> None:
        ced = Colors.style(Colors.BLUE, self.__EDITING_DIR)
        print("Current editing directory: " + ced)
        print("Enter a valid directory: ")
        user_input = input()
        print("Path Entered: ", user_input)
        if os.path.isdir(user_input):
            self.__EDITING_DIR = user_input
            success = Colors.style(Colors.GREEN, "Successfully")
            print(success + " updated")
            print("-> " + self.__EDITING_DIR)
        else:
            print("Error: Not a valid path")

    def get_missppelled_dir(self) -> str:
        return self.__MISSPELLED_DIR

    def get_current_config(self):
        current_dir = Colors.style(Colors.BLUE, self.__CURRENT_DIR)
        edit_dir = Colors.style(Colors.BLUE, self.__EDITING_DIR)
        pd = Colors.style(Colors.BLUE, self.__PARENT_PATH)
        print("Currenct directory: " + current_dir)
        print("Editing directory: " + edit_dir)
        print("Parent path: " + pd)


def main():
    print(os.getenv("PATH"))


# main()
