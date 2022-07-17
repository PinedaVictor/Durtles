

class ModOption:

    _OPTION_PREFIX = "-"

    def __init__(self) -> None:
        pass

    def add_prefix(self, option: str) -> str:
        return f"{self._OPTION_PREFIX}{option}"

    def remove_prefix(self, option: str) -> str:
        return option.replace(self._OPTION_PREFIX, "")
