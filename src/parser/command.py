
import parser.constants as c
import utils.colors as paint


class Command:

    color = paint.Colors()

    def __init__(self, cmd_arg) -> None:
        self.cmd = {} or ""
        self.valid(cmd_arg)

    def valid(self, user_input: str) -> str or set:
        try:
            self.cmd = c.COMMANDS[user_input]
        except:
            self.cmd = self.invalid(user_input)

    def invalid(self, user_input: str) -> str:
        user_cmd_error = self.color.style(self.color.RED, user_input)
        user_feedback = f"{user_cmd_error} is not a valid command."
        return user_feedback
