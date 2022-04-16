#
# Victor Pineda
# Description: Goes through files in the layers directory
# and checks for spelling errors for file names.

import os
import re
from regex import F
from textblob import Word

print("With dictionary")
currentDir = os.getcwd()
parentPath = os.path.dirname(currentDir)
print("Parent Dir: " + parentPath)
editingDir = "{}/Layers".format(parentPath)
print("Editing Dir: " + editingDir)
print(" ")
pattern = re.compile("[a-zA-Z]* ?[^jpg|#|\d|.]")

all_files = {
    "name": "",
    "src": "",
}

incorrect_file_name = {
    "name": "",
    "src": "",
    "suggestions": []
}

i = []

incorrect_files = []

# ALG
# 1. place all file names in a set
# 2. Check spelling for each name
# 3. place correct words in set A Let set B denote misspelled words
# 4.


def wD():
    for subDir, subFolderName, files in os.walk(editingDir):
        for file in files:
            src = "{0}/{1}".format(subDir, file)
            file_data = {"name": file, "src": src}
            i.append(file_data)


def checkAllFileNames():
    print("Checking all files name")

    for fileData in i:
        find_file_name = pattern.findall(fileData["name"])
        name = ''.join(find_file_name)
        full_name = name.split()
        # is_name_correct = isFileNameCorrect(full_name)
        # print(full_name)

        # print(len(full_name))
        # print(is_name_correct)
        if(len(full_name) < 2):
            # print(full_name[0])
            is_name_correct = checkWord(full_name[0])
            print(is_name_correct)

        # if(len(is_name_correct) > 0):
        #     print("We have suggestions")
        #     print(is_name_correct)


def checkWord(file_name):
    print(" ")
    check_spelling = Word(file_name)
    possible_words = check_spelling.spellcheck()

    if(len(possible_words) == 1 and possible_words[0][1] == 0.0):
        word_suggestions = possible_words
        return word_suggestions

    for word in possible_words:
        if(word[0] == file_name):
            word_suggestions = []
            return word_suggestions

    return possible_words


def accepter():
    print("Running")
    wD()
    checkAllFileNames()
    # l = ["Yellow Greafdsfen blue"]
    # check = checkFileName(l)
    # print(check)


accepter()
