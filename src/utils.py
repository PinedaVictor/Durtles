# Utility functions
from colors import Colors

HELP = Colors.style(Colors.GREEN, "-h")
PR = Colors.style(Colors.GREEN, "-pr")
R = Colors.style(Colors.GREEN, "-r")
C = Colors.style(Colors.GREEN, "-c")


class Utils:
    def display_help():
        print("Usage: python3 main.py [OPTIONS...]")
        options = Colors.style(Colors.GREEN, "Options:")
        print(options)
        print(f"     {HELP}      Display help menu")
        print(f"     {PR}     Preview files that will be renamed")
        print(f"     {R}      Rename files")
        print(f"     {C}      Count number of sub directories")


# TODO: Implement -V -version function
