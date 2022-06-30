
from ast import arg
import utils.colors as paint


class Error:

    color = paint.Colors()
    _HELP_MESSAGE = "Use drt -h or -help to view help menu."
    _DRT = color.drt()

    def __init__(self) -> None:
        self.error = ""

    def error_message(self, error: str, user_input="") -> str:
        error_flag = self.color.style_error(error)
        user_args = self.color.user_args(user_input)
        if user_input:
            self.error = f"{self._DRT} {error_flag} {user_args} {self._HELP_MESSAGE}"
        else:
            self.error = f"{self._DRT} {error_flag} {self._HELP_MESSAGE}"
        return self.error

    def no_args(self) -> str:
        return self.error_message("No Args provided.")

    def invalid_args(self, args) -> str:
        return self.error_message("Unrecognized Arguments", args)

    def option(self, option: str) -> str:
        option_error = self.color.style_error(option)
        feedback = f"Option: {option_error} is not a valid option."
        return feedback

    def cmd(self, cmd_input: str) -> str:
        cmd_error = self.color.style_error(cmd_input)
        feedback = f"{cmd_error} is not a valid command."
        return feedback

    def cmd_option():
        pass
