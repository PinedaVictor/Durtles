# Main function
import sys

import arg_parser
import parser.command as cmd

# def main():
#     parse_input = arg_parser.ArgParser()
#     parse_input.parse(sys.argv)


def main():
    print("Testing new parser")
    input = sys.argv
    # print(input[1])

    print("obj parsed")
    if(len(input) == 1):
        p = cmd.Command("")
        print(p.cmd)
    else:
        parse = cmd.Command(input[1])
        print(parse.cmd)
        print("This printed")
        return


if __name__ == '__main__':
    main()
