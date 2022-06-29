

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


import parse.mod_option as mod_pre
import parse.constants as c
import parse.command as cm
import parse.option as op


class Preprocess:

    def __init__(self, cmd_args: list) -> None:
        self.valid_args = "" or list
        self.valid_option = op.Option(cmd_args[1])
        self.valid_cmd = cm.Command(cmd_args[1])
        self.validate(cmd_args)

    def validate(self, cmd_args: list) -> list:
        # cases:
        #   1. only one option provided
        #       - length matters len = 1 = option or cmd
        #   2. one command plus option

        print("IN preprocess step")
        print(cmd_args)
        # option = self.is_option(cmd_args)

        print(self.valid_option.cmd_arg_option)
        print(self.valid_cmd.cmd)
        pass
