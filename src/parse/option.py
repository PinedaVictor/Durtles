
import parse.constants as c
import utils.colors as paint
import parse.mod_option as mod


class Option:

    color = paint.Colors()

    def __init__(self, cmd_arg: str) -> None:
        self.cmd_arg_option = ""
        self.valid(cmd_arg)

    def valid(self, option_arg: str) -> str:
        mod_option = mod.ModOption().remove_prefix(option_arg)
        if mod_option in c.BLANK_CMD_OPTIONS:
            self.cmd_arg_option = mod_option
        else:
            self.cmd_arg_option = self.invalid(option_arg)

    def invalid(self, option: str) -> str:
        option_error = self.color.style_error(option)
        feedback = f"Option: {option_error} is not a valid option."
        return feedback

    # TODO: write function for valid CMD Options
    def valid_cmd_option(self):
        pass
