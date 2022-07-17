#
# Victor Pineda
# Description: This will rename all files in the
# directory with the following pattern.
# Script parameters:
#   * Empty preview rename files
#   * -r rename all files in Layers directory

# TODO: implement -help argument option that prints CMD options for scripts

import re
import os
import utils.colors as color
import utils.global_ as globals

NAME_PATTERN = re.compile(
    "[a-zA-Z]* ?-?[a-zA-Z]* ?-?[\s]?[a-zA-Z]*[#][(\d+(?:\.\d+)?)]*[-]?.[a-zA-Z]*")
remove_underscore_dash = "_*-*"

EDITING_DIR = globals.EDITING_DIR
Colors = color.Colors()


# TODO: FIXME: ENSURE PROPER class design -> every class function should have a self parameter
# FIXME: Reduntant code
class Rename:

    def rename(self):
        for sub_dir, sub_folder_name, files in os.walk(EDITING_DIR):
            for file in files:
                src = "{0}/{1}".format(sub_dir, file)
                find_pattern = NAME_PATTERN.findall(file)
                temp_name = ''.join(find_pattern)
                new_name = re.sub(remove_underscore_dash, '', temp_name)
                dist = "{0}/{1}".format(sub_dir, new_name)
                os.rename(src, dist)

    def preview_rename(self):
        for sub_dir, sub_folder_name, files in os.walk(EDITING_DIR):
            print("In directory: " + sub_dir)
            for file in files:
                file_st = Colors.style(Colors.BLUE, "File:")
                file_name = Colors.style(Colors.YELLOW, file)
                find_pattern = NAME_PATTERN.findall(file)
                temp_name = ''.join(find_pattern)
                new_name = re.sub(remove_underscore_dash, '', temp_name)
                name_st = Colors.style(Colors.BLUE, "New Name: ")
                new_name_st = Colors.style(Colors.GREEN, new_name)
                print(file_st + " " + file_name)
                print(name_st + " " + new_name_st)
                print(" ")

    def ops(self) -> dict:
        ops = {
            "r": "rename",
            "pr": "preview_rename"
        }
        return ops
