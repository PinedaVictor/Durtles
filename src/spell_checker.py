#
# Victor Pineda
# Description: Goes through files in the layers directory
# and checks for spelling errors for file names.
# Arguments:
# -s Seperate misspelled words in a directory called Misspelled

import os
import re
import shutil
import utils.colors as color
from textblob import Word
import utils.global_ as globals


# TODO: You may not need re for this - look into the os lib
#       their is a function call that returns only the name

PATTERN = re.compile("[a-zA-Z]* ?[^jpg|#|\d|.]")
EDITING_DIR = globals.EDITING_DIR
MISSPELLED_DIR = globals.MISSPELLED_DIR
Colors = color.Colors()


class SpellChecker:

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

    def __init__(self) -> None:
        self.init_file_system()
        self.check_all_file_names()

    def init_file_system(self):
        for subDir, subFolderName, files in os.walk(EDITING_DIR):
            for file in files:
                src = "{0}/{1}".format(subDir, file)
                file_data = {"name": file, "src": src}
                self.file_system.append(file_data)

    def check_all_file_names(self):
        for fileData in self.file_system:
            find_file_name = PATTERN.findall(fileData["name"])
            name = ''.join(find_file_name)
            full_name = name.split()

            if(len(full_name) < 2):
                word_suggestions = self.check_word(full_name[0])
                incorrect = {
                    "name": full_name[0], "src": fileData["src"], "suggestions": word_suggestions}
                if(len(word_suggestions) != 0):
                    self.incorrect_files.append(incorrect)
            else:
                for word in full_name:
                    getting_word_suggest = self.check_word(word)
                    incorrect_word = {
                        "name": word, "src": fileData["src"], "suggestions": getting_word_suggest}
                    if(len(getting_word_suggest) != 0):
                        self.incorrect_files.append(incorrect_word)

    def print_errors(self):
        num_errors = Colors.style(Colors.RED, str(len(self.incorrect_files)))
        print(f"{num_errors} Errors found: Use -ss to seperate them")
        for file in self.incorrect_files:
            spelling_error = Colors.style(Colors.RED, file["name"])
            print(spelling_error)

    def seperate_incorrect_directory(self):
        incorrect_name_src = set()

        for data in self.incorrect_files:
            incorrect_name_src.add(data["src"])

        if not os.path.isdir(MISSPELLED_DIR):
            os.mkdir(MISSPELLED_DIR)

        for path in incorrect_name_src:
            folder = os.path.dirname(path)
            file_name = os.path.basename(path)
            folder_dir = folder.replace(EDITING_DIR, '')
            out_dir = "{0}{1}".format(MISSPELLED_DIR, folder_dir)
            move_file = "{0}/{1}".format(out_dir, file_name)
            print(move_file)
            if not os.path.isdir(out_dir):
                os.mkdir(out_dir)
                shutil.move(path, move_file)
            else:
                shutil.move(path, move_file)

    def migrate_misspelled_dir(self):

        if not os.path.isdir(MISSPELLED_DIR):
            print(
                "You either have no spelling errors or you have not ran python3 spellchecker.py -ss")
            print(
                "python3 spellchecker.py -ss will move misspelled file names to directory Misspelled")
        else:
            print("Migrating")
            print("")

            for sub_dir, sub_folder_name, files in os.walk(MISSPELLED_DIR):
                for file in files:
                    src = "{0}/{1}".format(sub_dir, file)
                    folder_of_file = sub_dir.replace(MISSPELLED_DIR, '')
                    og_dir = "{0}{1}/{2}".format(EDITING_DIR,
                                                 folder_of_file, file)

                    shutil.move(src, og_dir)

        shutil.rmtree(MISSPELLED_DIR)

    def check_word(self, file_name):
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

    def print_suggestions(self):
        for incorrect_data in self.incorrect_files:
            print("src: " + incorrect_data["src"])
            print("word: " + incorrect_data["name"])
            print("Did you mean: ")
            for i in range(0, len(incorrect_data["suggestions"])):
                print(str(i+1) + ": " +
                      incorrect_data["suggestions"][i][0] + " ", end="")
            print()
            print("")

    def check_errors(self):
        if(len(self.incorrect_files) < 1):
            return "No spelling erros found"
        else:
            return "Errors Found"
