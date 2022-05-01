# Main function
import sys
from arg_parser import ArgParser


def main():
    parse_input = ArgParser()
    parse_input.parse(sys.argv)


if __name__ == '__main__':
    main()
