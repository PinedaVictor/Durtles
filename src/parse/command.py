
import parse.constants as c


class Command:

    def __init__(self, cmd_arg: list) -> None:
        self.cmd = {} or False
        self.valid(cmd_arg[1])

    def valid(self, cmd_input: str) -> str or set:
        try:
            self.cmd = c.COMMANDS[cmd_input]
        except:
            self.cmd = False
