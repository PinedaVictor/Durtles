
import parse.command as cm
import parse.option as op
import parse.error as er
import parse.parse_option as po


class Parse:

    error = er.Error()

    def __init__(self, cmd_args: list) -> None:
        self.assign_args(cmd_args)

    def assign_args(self, args: list) -> None:
        print(len(args))
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
            print("Valid cmd ")
            self.valid_cmd
        else:
            # PARSE OPTION
            self.valid_option
            po.ParseOption(self.valid_option.option)
            # self.help_user.execute(self.valid_option.option)


# This step is acting like my parser => may not need another one on top of this
# At this point we have a valid option or cmd or niether
# BLOG POST: https://betterprogramming.pub/optimize-your-python-codebases-by-2-5x-with-direct-attribute-access-410df06ec46e
# Refernce the blog post to assing local vars to functions

# alg
# for each cmd or option
    # generate dict of {key = option, value = function }
# once generated you can execute function given it's key

# FIRST STEP: run -h option or the default for a cmd
