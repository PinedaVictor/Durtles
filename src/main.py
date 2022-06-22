# Main function
import sys
import arg_parser


def main():
    parse_input = arg_parser.ArgParser()
    parse_input.parse(sys.argv)


if __name__ == '__main__':
    main()
