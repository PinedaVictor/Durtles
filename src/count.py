#
# Victor Pineda
# Description: List all folders in the Layers directory.

import os
import utils.global_ as globals
import utils.colors as color


Colors = color.Colors()


def count_folders_dir():
    try:
        num_of_folders = Colors.style(
            Colors.GREEN, str(len(os.listdir(globals.EDITING_DIR))))
        print(num_of_folders)
    except:
        if not os.path.isdir(globals.EDITING_DIR):
            print("Directory does not exist")
        else:
            print("Error has occurred")
