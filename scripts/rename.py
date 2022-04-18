#
# Victor Pineda
# Description: This will rename all files in the
# layers directory with the following pattern.
# Script parameters
#   * Empty preview rename files
#   * -r rename all files in Layers directory

# TODO: implement -help argument option that prints CMD options for scripts

import re
import os
import sys
from global_ import PARENT_PATH
from global_ import EDITING_DIR

NAME_PATTERN = re.compile(
    "[a-zA-Z]* ?-?[a-zA-Z]* ?-?[\s]?[a-zA-Z]*[#][(\d+(?:\.\d+)?)]*[-]?.[a-zA-Z]*")
remove_underscore_dash = "_*-*"


def rename():
    print("Parent directory: " + PARENT_PATH)
    print("Editing Directory: " + EDITING_DIR)
    print(" ")

    for sub_dir, sub_folder_name, files in os.walk(EDITING_DIR):
        for file in files:
            src = "{0}/{1}".format(sub_dir, file)
            find_pattern = NAME_PATTERN.findall(file)
            temp_name = ''.join(find_pattern)
            new_name = re.sub(remove_underscore_dash, '', temp_name)
            dist = "{0}/{1}".format(sub_dir, new_name)
            os.rename(src, dist)


def preview_rename():
    print("Preview Rename")
    print(" ")

    for sub_dir, sub_folder_name, files in os.walk(EDITING_DIR):
        print("In directory: " + sub_dir)
        for file in files:
            print("File: " + file)
            src = "{0}/{1}".format(sub_dir, file)
            print("src: " + src)
            find_pattern = NAME_PATTERN.findall(file)
            temp_name = ''.join(find_pattern)
            new_name = re.sub(remove_underscore_dash, '', temp_name)
            print("New Name: " + new_name)
            dist = "{0}/{1}".format(sub_dir, new_name)
            print("Dist: " + dist)
            print(" ")


def accepter():

    arg_length = len(sys.argv)

    if(arg_length == 1):
        preview_rename()
    else:
        try:
            argument = str(sys.argv[1])
            if(argument == "-r"):
                rename()
            else:
                print("ERROR: Argument does not exist")
                print("Either run defualt script or choose an acceptable argument")
        except:
            print("Error: Make sure your input is in the correct format ")


accepter()
