#
# Victor Pineda
# Description: List all folders in the Layers directory.

import os
from global_ import EDITING_DIR
from colors import Colors


def count_folders_dir():
    try:
        num_of_folders = Colors.style(
            Colors.GREEN, str(len(os.listdir(EDITING_DIR))))
        print(num_of_folders)
    except:
        if not os.path.isdir(EDITING_DIR):
            print("Directory does not exist")
        else:
            print("Error has occurred")
