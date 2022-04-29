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
import sys
from colors import Colors
from global_ import EDITING_DIR

app = typer.Typer()

NAME_PATTERN = re.compile(
    "[a-zA-Z]* ?-?[a-zA-Z]* ?-?[\s]?[a-zA-Z]*[#][(\d+(?:\.\d+)?)]*[-]?.[a-zA-Z]*")
remove_underscore_dash = "_*-*"


class Rename:

    def rename():
        for sub_dir, sub_folder_name, files in os.walk(EDITING_DIR):
            for file in files:
                src = "{0}/{1}".format(sub_dir, file)
                find_pattern = NAME_PATTERN.findall(file)
                temp_name = ''.join(find_pattern)
                new_name = re.sub(remove_underscore_dash, '', temp_name)
                dist = "{0}/{1}".format(sub_dir, new_name)
                os.rename(src, dist)

    def preview_rename():
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


# TODO: Verify this accepter funciton is no longer needed
#       might be wise to keep for local testing


    def accepter():

        arg_length = len(sys.argv)

        if(arg_length == 1):
            Rename.preview_rename()
        else:
            try:
                argument = str(sys.argv[1])
                if(argument == "-r"):
                    Rename.rename()
                else:
                    print("ERROR: Argument does not exist")
                    print("Either run defualt script or choose an acceptable argument")
            except:
                print("Error: Make sure your input is in the correct format ")

# accepter()


# @app.command("dir")
# def main(r: str = typer.Option(None, help="Preview files that will be renamed")):
#     print("All the way ")
#     if(r):
#         preview_rename()

@app.command("dir")
def main(pr: str = typer.Option(None, help="Preview files that will be renamed"), arg: str = typer.Argument(None, help="the")):
    print("All the way ")
    if(pr):
        print(pr)
        # preview_rename()


if __name__ == "__main__":
    app()
