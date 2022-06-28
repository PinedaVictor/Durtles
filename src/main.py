# Main function
import sys

# import arg_parser
# import parser.command as cmd
import parser.option as cmd

# def main():
#     parse_input = arg_parser.ArgParser()
#     parse_input.parse(sys.argv)


def main():

    input = sys.argv

    if(len(input) == 1):
        p = cmd.Option("")
        print(p.cmd_arg_option)
    else:
        print("Calling option")
        parse = cmd.Option(input[1])
        print("Option: " + parse.cmd_arg_option)
        return


if __name__ == '__main__':
    main()
