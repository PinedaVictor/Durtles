
import parse.constants as c
import parse.mod_option as mod


class Option:

    def __init__(self, cmd_arg: list) -> None:
        self.option = "" or False
        self.valid(cmd_arg[1])

    def valid(self, option_arg: str) -> str or bool:
        mod_option = mod.ModOption().remove_prefix(option_arg)
        if mod_option in c.BLANK_CMD_OPTIONS:
            self.option = mod_option
        else:
            self.option = False

    # TODO: write function for valid CMD Options
    def valid_cmd_option(self):
        pass
