# Main function
import sys


import parse.parse as parse

# def main():
#     parse_input = arg_parser.ArgParser()
#     parse_input.parse(sys.argv)


def main():

    input = sys.argv
    # print(input)
    # pr.Preprocess(input)
    parse.Parse(input)


if __name__ == '__main__':
    main()
