#
# Victor Pineda
# Description: List all folders in the Layers directory.

import os
import typer
from global_ import EDITING_DIR


def count_folders_dir():
    try:
        num_of_folders = len(os.listdir(EDITING_DIR))
        typer.secho(num_of_folders, fg=typer.colors.GREEN)
    except:
        if not os.path.isdir(EDITING_DIR):
            print("Directory does not exist")
        else:
            print("Error has occurred")
