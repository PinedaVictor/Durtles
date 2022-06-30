

# Steps needed
# 1. validate user input params [CMD | OPTION] OPTION
#   1.1 valid CMD or OPTION
#   1.2 if OPTION
#       1.2.1 call function
#   1.3 call CMD
#       1.3.1 if OPTION provided call function
# 2. Setup up function execution

# preprocess
# what should it return?
# Do I need a preprocess step?
# Should I parse at this step and avpid preprocess?


from distutils.log import error
import parse.command as cm
import parse.option as op
import parse.error as er


class Preprocess:

    error = er.Error()

    def __init__(self, cmd_args: list) -> None:
        self.valid_args = "" or list
        self.valid_cmd = "" or bool
        self.valid_cmd = "" or bool
        self.assign_args(cmd_args)

    def assign_args(self, args: list) -> None:
        if len(args) != 1:
            self.valid_option = op.Option(args)
            self.valid_cmd = cm.Command(args)
            self.validate(args)
        else:
            print(self.error.no_args())

    def validate(self, args) -> None:
        cmd = self.valid_cmd.cmd
        option = self.valid_option.cmd_arg_option
        print(cmd)
        print(option)
        if cmd == False and option == False:
            print(self.error.invalid_args(f"{args[1]}"))
        elif cmd != False:
            print("Parse cmd")
            print(cmd)
        else:
            print("Parse option")
            print(option)
