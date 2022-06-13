# Victor Pineda
# Description: Hold vairbbals needed for most python modules

import os
# TODO: Migrate to drt config once ready
CURRENT_DIR = os.getcwd()
PARENT_PATH = os.path.dirname(CURRENT_DIR)
EDITING_DIR = "{0}/Edit".format(PARENT_PATH)
MISSPELLED_DIR = "{0}/Misspelled".format(PARENT_PATH)
