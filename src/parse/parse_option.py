

import help_menu as hm


BLANK_CMD_OPTIONS = {"help", "h", "V", "v", "c", "version", "pr", "r"}


class ParseOption(hm.HelpMenu):

    help_user = hm.HelpMenu().getOperations()

    def __init__(self, option: str) -> None:
        print("Parsing option")
        print(option)
        self.resolve(option)
        pass

    def resolve(self, option: str):
        func = getattr(self, self.help_user[option])
        func()
        pass
