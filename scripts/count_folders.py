#
# Victor Pineda
# Description: List all folders in the Layers directory.


import os
from global_ import EDITING_DIR


def countFolders():
    try:
        print(len(os.listdir(EDITING_DIR)))
    except:
        if not os.path.isdir(EDITING_DIR):
            print("Directory does not exist")
        else:
            print("Error has occurred")


countFolders()
