

import parse.operations as op

BLANK_CMD_OPTIONS = {"help", "h", "V", "v", "c", "version", "pr", "r"}


class Process(op.Operations):

    ops = op.Operations().get_ops()

    def __init__(self) -> None:
        pass

    def option(self, option: str) -> None:
        func = getattr(self, self.ops[option])
        func()

    def command(self, args: list) -> None:
        func = getattr(self, self.ops[args[0]][args[1]])
        func()
