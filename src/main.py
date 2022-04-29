# Main function
import sys
from arg_parser import ArgParser


def main():
    arg_length = len(sys.argv)
    # Check if their ar no args
    if(arg_length == 1):
        print("drt: try python3 main.py -help")
    else:
        input_option = sys.argv[1]
        ArgParser.parse(input_option)


if __name__ == '__main__':
    main()
