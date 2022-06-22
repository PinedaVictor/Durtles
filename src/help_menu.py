# Utility functions
import utils.colors as color
Colors = color.Colors()


# options
# TODO: This can be abstracted out into a function
HELP = Colors.style(Colors.GREEN, "-h")
PR = Colors.style(Colors.GREEN, "-pr")
R = Colors.style(Colors.GREEN, "-r")
C = Colors.style(Colors.GREEN, "-c")
SS = Colors.style(Colors.GREEN, "-ss")
M = Colors.style(Colors.GREEN, "-m")
SC = Colors.style(Colors.GREEN, "-sc")
PS = Colors.style(Colors.GREEN, "-ps")
E = Colors.style(Colors.GREEN, "-e")


# Commands
# TODO: This can be abstracted out into a function
config = Colors.style(Colors.BLUE, "config")
check = Colors.style(Colors.BLUE, "check")

# FIXME: Rename this class - confusing with the package


class Utils:
    def display_help(self):
        print("Usage: python3 main.py [OPTIONS...]")
        options = Colors.style(Colors.GREEN, "Options:")
        print(options)
        print(f"     {HELP}      Display help menu")
        print(f"     {PR}     Preview files that will be renamed")
        print(f"     {R}      Rename files")
        print(f"     {C}      Count number of sub directories")
        print("Usage: python3 main.py [COMMAND...][OPTIONS...]")
        cmds = Colors.style(Colors.BLUE, "Commands:")
        print(cmds)
        print(f"     {config}   Edit config")
        print(f"     {check}    Spell checker")

    def display_check_help(self):
        check = Colors.style(Colors.BLUE, "check")
        print(f"Usage: python3 main.py {check} [OPTIONS...]")
        print("    None     Prints Errors found")
        print(f"     {PS}     Print suggestions")
        print(
            f"     {SS}     Seperate misspelled files into the misspelled directory")
        print(
            f"     {M}      Migrate files in the misspelled directory back to their origin")
        print(f"     {HELP}      Print this message")

    def display_config_help(self):
        config = Colors.style(Colors.BLUE, "config")
        print(f"Usage: python3 main.py {config} [OPTIONS...]")
        print("   None      Print current config")
        print(f"     {HELP}      Print this message")
        # TODO: This needs to be implemented correctly
        # print(f"     {E}      Change editing directory")


# TODO: Implement -V -version function
