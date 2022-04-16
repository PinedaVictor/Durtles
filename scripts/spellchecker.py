#
# Victor Pineda
# Description: Goes through files in the layers directory
# and checks for spelling errors for file names.

import os
import re
import shutil
from textblob import Word

print("With dictionary")
CURRENT_DIR = os.getcwd()
PARENT_PATH = os.path.dirname(CURRENT_DIR)
print("Parent Dir: " + PARENT_PATH)
EDITING_DIR = "{}/Layers".format(PARENT_PATH)
print("Editing Dir: " + EDITING_DIR)
print(" ")

PATTERN = re.compile("[a-zA-Z]* ?[^jpg|#|\d|.]")

all_files = {
    "name": "",
    "src": "",
}

incorrect_file_name = {
    "name": "",
    "src": "",
    "suggestions": []
}

file_system = []

incorrect_files = []


def init_file_system():
    for subDir, subFolderName, files in os.walk(EDITING_DIR):
        for file in files:
            src = "{0}/{1}".format(subDir, file)
            file_data = {"name": file, "src": src}
            file_system.append(file_data)


def check_all_file_names():
    for fileData in file_system:
        find_file_name = PATTERN.findall(fileData["name"])
        name = ''.join(find_file_name)
        full_name = name.split()

        if(len(full_name) < 2):
            word_suggestions = check_word(full_name[0])
            incorrect = {
                "name": full_name[0], "src": fileData["src"], "suggestions": word_suggestions}
            if(len(word_suggestions) != 0):
                incorrect_files.append(incorrect)
        else:
            for word in full_name:
                getting_word_suggest = check_word(word)
                incorrect_word = {
                    "name": word, "src": fileData["src"], "suggestions": getting_word_suggest}
                if(len(getting_word_suggest) != 0):
                    incorrect_files.append(incorrect_word)


def check_word(file_name):
    check_spelling = Word(file_name)
    possible_words = check_spelling.spellcheck()

    if(len(possible_words) == 1 and possible_words[0][1] == 0.0):
        word_suggestions = ["Unknown Word"]
        return word_suggestions

    for word in possible_words:
        if(word[0] == file_name):
            word_suggestions = []
            return word_suggestions

    return possible_words


def print_incorrect():
    for incorrect_data in incorrect_files:
        print("src: " + incorrect_data["src"])
        print("word: " + incorrect_data["name"])
        print("Did you mean: ")
        for i in range(0, len(incorrect_data["suggestions"])):
            print(str(i+1) + ": " +
                  incorrect_data["suggestions"][i][0] + " ", end="")
        print()
        print("")


def accepter():
    init_file_system()
    check_all_file_names()
    print_incorrect()


accepter()
