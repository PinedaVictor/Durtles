

import help_menu as hm
import count as c
import parse.operations as op

BLANK_CMD_OPTIONS = {"help", "h", "V", "v", "c", "version", "pr", "r"}


class ParseOption(op.Operations):

    ops = op.Operations().get_ops()

    def __init__(self, option: str) -> None:
        self.resolve(option)

    def resolve(self, option: str) -> None:
        func = getattr(self, self.ops[option])
        func()
