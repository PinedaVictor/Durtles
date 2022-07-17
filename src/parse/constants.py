

# These no CMD options

# COMMANDS = {"config", "check"}
# create dictionary of CMDs
# for every CMD there are an array xof options


# User interface is this:
# Current:
# python3 main.py [CMD | OPTION] [OPTION]
# Goal:
# drt [CMD | OPTION] [OPTION]

# commands module
# Have dictionary of commands  {key: value} where key = CMD and value =  {...OPTIONS}
#


# COMMANDS = {"config", "check"}

# TODO: Arg parser should account for leading slash ex. -V
# TODO: Handle blank input

OPTION_PREFIX = "-"
BLANK_CMD_OPTIONS = {"help", "h", "V", "v", "c", "version", "pr", "r"}
CHECK_OPTIONS = {"", "ps", "ss", "m", "h"}

COMMANDS = {"": BLANK_CMD_OPTIONS, "check": CHECK_OPTIONS}
