
import os
from count import count_folders_dir
from utils import Utils
from colors import Colors
from rename import Rename
from spell_checker import SpellChecker
from config import DrtConfig
# Interprest cmd string argument
# and execute cmd

OPTIONS = {"-help", "-h", "-V", "-c",
           "-version", "-pr", "-r"}
COMMANDS = {"config", "check"}

# input format goal drt option or drt cmd arg
DEFAULT_EDIT_DIR = "{0}/Edit".format(os.path.dirname(os.getcwd()))
sc = SpellChecker()
drt = DrtConfig(edit_directory=DEFAULT_EDIT_DIR)


class ArgParser:

    def parse(self, args: list):
        args_length = len(args)
        if(args_length == 1):
            print("drt: try python3 main.py -h")
        else:
            if(args_length == 2 and args[1] in OPTIONS):
                self.parse_option(args[1])
            elif(args_length > 1 and args[1] in COMMANDS):
                self.parse_command(args)
            else:
                self.error_parsing(args[1])

    def parse_option(self, option: str):
        if(option == "-help" or option == "-h"):
            Utils.display_help()
        elif(option == "-c"):
            count_folders_dir()
        elif(option == "-pr"):
            Rename.preview_rename()
        elif(option == "-r"):
            Rename.rename()
        elif(option == "-sc"):
            sc.check_all_file_names()

    def parse_command(self, args: list):
        # FIXME: Account for longer option input
        cmd = args[1]
        if len(args) == 2:
            option = ""
            # FIXME: Call another function
        elif len(args) == 3:
            option = args[2]
        else:
            input_cmd = Colors.style(Colors.RED, cmd)
            print("Error parsing command: " + input_cmd)
            return

        if(cmd == "check"):
            if(option == ""):
                sc.print_errors()
            elif(option == "-h" or option == "-help"):
                Utils.display_check_help()
            elif(option == "-ss"):
                sc.seperate_incorrect_directory()
            elif(option == "-m"):
                sc.migrate_misspelled_dir()
            elif(option == "-ps"):
                sc.print_suggestions()
            else:
                self.error_parsing(option)

        if(cmd == "config"):
            if(option == ""):
                drt.get_current_config()
            elif(option == "-h" or option == "-help"):
                Utils.display_config_help()
            else:
                self.error_parsing(option)

    def error_parsing(self, arg):
        user_arg = Colors.style(Colors.RED, arg)
        print(
            f"Option {user_arg} does not exists: Use -help to view availble options")
