
# Parse CMD arguments

from count import count_folders_dir
from utils import Utils
from colors import Colors
from rename import Rename
# Interprest cmd string argument
# and execute cmd

OPTIONS = {"-help", "-h", "-V", "-c", "-version", "-pr", "-r"}
COMMANDS = {"config"}

# input format goal drt option or drt cmd arg


class ArgParser:
    def parse(arg: str):
        print("In ArgParser parse function")
        print(arg)
        print()

        # Easy to check if cmd exists
        if arg in OPTIONS:
            if(arg == "-help" or arg == "-h"):
                Utils.display_help()
            elif(arg == "-c"):
                count_folders_dir()
            elif(arg == "-pr"):
                Rename.preview_rename()
            elif(arg == "-r"):
                Rename.rename()
        else:
            user_arg = Colors.style(Colors.RED, arg)
            print(
                f"Option {user_arg} does not exists: Use -help to view availble options")

        # NOW how can we call function based on that arg
