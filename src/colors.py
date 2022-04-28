# Class for color printing
class Colors:
    RED = "\u001b[31m"
    BLACK = "\u001b[30;1m"
    GREEN = "\u001b[32;1m"
    YELLOW = "\u001b[33;1m"
    BLUE = "\u001b[34;1m"
    MAGENTA = "\u001b[35;1m"
    CYAN = "\u001b[36;1m"
    WHITE = "\u001b[37;1m"
    RESET = "\u001b[0m"

    RED_BACKGROUND = "\u001b[1;37;41m"
    BLUE_BACKGROUND = "\u001b[1;37;44m"

    def color_text(color: str, statement: str):
        return color + statement + Colors.RESET
