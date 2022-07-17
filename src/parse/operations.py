

import help_menu as hm
import count as c
import rename as r
import spell_checker as sc


class Operations(hm.HelpMenu, c.Count, r.Rename, sc.SpellChecker):

    ops = {**hm.HelpMenu().ops(), **c.Count().ops(), **r.Rename().ops()}

    def __init__(self) -> None:
        pass

    def get_ops(self) -> dict:
        return self.ops
