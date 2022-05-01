
from count import count_folders_dir
from utils import Utils
from colors import Colors
from rename import Rename
from spell_checker import SpellChecker
# Interprest cmd string argument
# and execute cmd

OPTIONS = {"-help", "-h", "-V", "-c",
           "-version", "-pr", "-r"}
COMMANDS = {"config", "check"}

# input format goal drt option or drt cmd arg
sc = SpellChecker()


class ArgParser:

    def parse(self, args: list):
        args_length = len(args)
        if(args_length == 2 and args[1] in OPTIONS):
            self.parse_option(args[1])
        elif(args_length > 1 and args[1] in COMMANDS):
            self.parse_command(args)
        else:
            user_arg = Colors.style(Colors.RED, args[1])
            print(
                f"Option {user_arg} does not exists: Use -help to view availble options")

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
        cmd = args[1]
        if len(args) == 2:
            option = ""
        elif len(args) == 3:
            option = args[2]
        else:
            print("Error parsing CMD")

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
                print("Error reading option")
