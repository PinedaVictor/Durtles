#
# Victor Pineda
# Description: List all folders in the Layers directory.

import os
from global_ import EDITING_DIR


def count_folders_dir():
    """
     Count number of folders in a directory.
    """
    try:
        num_of_folders = len(os.listdir(EDITING_DIR))
        print(num_of_folders)
        # typer.secho(num_of_folders, fg=typer.colors.GREEN)
    except:
        if not os.path.isdir(EDITING_DIR):
            print("Directory does not exist")
        else:
            print("Error has occurred")
