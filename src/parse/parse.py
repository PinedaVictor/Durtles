
import parse.command as cm
import parse.option as op
import parse.error as er
import parse.process as po
import parse.mod_option as mod


class Parse:

    error = er.Error()
    m = mod.ModOption()

    def __init__(self, cmd_args: list) -> None:
        self.assign_args(cmd_args)

    def assign_args(self, args: list) -> None:
        if len(args) != 1:
            self.valid_option = op.Option(args)
            self.valid_cmd = cm.Command(args)
            self.validate(args)
        else:
            print(self.error.no_args())
            return

    def validate(self, args: list) -> None:
        if self.valid_cmd.cmd == False and self.valid_option.option == False:
            print(self.error.invalid_args(f"{args[1]}"))
            return
        elif self.valid_cmd.cmd != False:
            # PARSE CMD
            new_args = []
            if len(args) > 3:
                print(self.error.invalid_args(f"{args[1]}"))
                return
            elif len(args) == 2:
                new_args = [args[1], ""]
            elif len(args) == 3:
                new_args = [args[1], self.m.remove_prefix(args[2])]

            po.Process().command(new_args)

        else:
            # PARSE OPTION
            self.valid_option
            po.Process().option(self.valid_option.option)


# This step is acting like my parser => may not need another one on top of this
# At this point we have a valid option or cmd or niether
# BLOG POST: https://betterprogramming.pub/optimize-your-python-codebases-by-2-5x-with-direct-attribute-access-410df06ec46e
# Refernce the blog post to assing local vars to functions

# alg
# for each cmd or option
    # generate dict of {key = option, value = function }
# once generated you can execute function given it's key

# FIRST STEP: run -h option or the default for a cmd
