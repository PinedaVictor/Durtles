# Main function
import sys


import parse.preprocess as pr

# def main():
#     parse_input = arg_parser.ArgParser()
#     parse_input.parse(sys.argv)


def main():

    input = sys.argv
    # print(input)
    pr.Preprocess(input)


if __name__ == '__main__':
    main()
