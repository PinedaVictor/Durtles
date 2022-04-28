# Main function
import sys
from colors import Colors
from count import count_folders_dir
# import count
# from rename import preview_rename


OPTIONS = {"-help", "-h", "-V", "-c", "-version", }
COMMANDS = {"config"}


def main():
    arg_length = len(sys.argv)

    # Check if their ar no args
    if(arg_length == 1):
        print("drt: try drt -help")
    else:
        input_option = sys.argv[1]

    # Check if it exists in the
        if(input_option in OPTIONS):
            print(input_option)
            print("Option exists")
            # Run function based on option input
            if(input_option == "-help" or input_option == "-h"):
                print("Usage: drt [OPTIONS...]")
                s = Colors.style(Colors.RED, "S")
                sr = Colors.style(Colors.RED_BACKGROUND, "r")
                print(sr)
                print("Options:")
                print(s + "wassip")
                print("     -h      Display help menu")
                print("     -pr     Preview files that will be renamed")
                print("     -r      Rename files")
            elif(input_option == "-c"):
                print("calling count")
                count_folders_dir()
                # print_help()

        else:
            print(input_option)
            print(OPTIONS)
            print("Option does not exists: Use --help for availble option")


if __name__ == '__main__':
    main()
