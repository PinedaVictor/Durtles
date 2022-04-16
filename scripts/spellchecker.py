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
    "correct": False
}

incorrect_file_name = {
    "name": "",
    "src": "",
    "suggestions": []
}

i = []


def runSpellChecker():
    for subDir, subFolderName, files in os.walk(editingDir):
        print("In directory: " + subDir)
        for file in files:
            print("File: " + file)
            # src = "{0}/{1}".format(subDir, file)
            # print("src: " + src)
            findPattern = pattern.findall(file)
            checkName = ''.join(findPattern)
            # newName = re.sub(removeUndeDash, '', tempName)
            print("Checking name: " + checkName)
            checkFileName(checkName)
            print("-----")
            # dist = "{0}/{1}".format(subDir, newName)
            # print("Dist: " + dist)
        print(" ")

# spellcheck()

# ALG
# 1. place all file names in a set
# 2. Check spelling for each name
# 3. place correct words in set A Let set B denote misspelled words
# 4.


def initFileSystem():
    for subDir, subFolderName, files in os.walk(editingDir):
        for file in files:
            src = "{0}/{1}".format(subDir, file)
            filedata = (file, src)
            all_files.add(filedata)
# initFileSystem()


def wD():
    for subDir, subFolderName, files in os.walk(editingDir):
        for file in files:
            src = "{0}/{1}".format(subDir, file)
            file_data = {"name": file, "src": src, "correct": True}
            i.append(file_data)


def checkAllFileNames():
    print("Checking all files name")

    for fileData in i:
        find_file_name = pattern.findall(fileData["name"])
        name = ''.join(find_file_name)
        full_name = name.split()
        is_name_correct = isFileNameCorrect(full_name)
        print(full_name)
        print(is_name_correct)

        # if(len(is_name_correct) > 0):
        #     print("We have suggestions")
        #     print(is_name_correct)


def isFileNameCorrect(file_name):
    print(" ")
    file_name_length = len(file_name)
    word_suggestions = []

    truthiness = []

    if(file_name_length < 2):
        check_spelling = Word(file_name[0])
        possible_words = check_spelling.spellcheck()
        if(len(possible_words) == 1 and possible_words[0][1] == 0.0):
            truthiness.append(False)
            word_suggestions = possible_words
        else:
            for word in possible_words:
                if(word[0] == file_name[0]):
                    truthiness.append(True)
                else:
                    truthiness.append(False)
                    word_suggestions = possible_words

    else:
        print("Name longer than 1")
        print(file_name)
        # print(" ")

    # for file_name_word in file_name:
    #     # print("Checking word : " + file_name_word)
    #     check_word = Word(file_name_word)
    #     possible_corrections = check_word.spellcheck()
    #     # print(possible_corrections)
    #     # print(str(len(possible_corrections)))
    #     # print(possible_corrections[0][1] == 0.0)

    #     # Check unkown word
    #     if(len(possible_corrections) == 1 and possible_corrections[0][1] == 0.0):
    #         # print("Unkown Word 🧐")
    #         correctness_values.append(False)
    #     else:
    #         for word in possible_corrections:
    #             # print(possible_corrections)
    #             # print("In my else clause")
    #             # print(word[0])
    #             if(word[0] == file_name_word):
    #                 # print("checking for correct word: " + word)
    #                 # print(file_name_word + " : " + word[0])
    #                 correctness_values.append(True)
    #                 # print("Looks good: ✅")
    #                 # correctness_values.add(False)
    #                 # print(file_name_correct)
    #             else:
    #                 correctness_values.append(False)
    #     # TODO: Going to need to add truth values to a set or list
    #     #       and final loop to see if there are any False
    #     #       values. If there are False values, there is spelling errors

    a = set(truthiness)

    if(True in a):
        # print("Coorrect: ")
        return []
    else:
        # print("word is incorrect")
        return word_suggestions


def accepter():
    print("Running")
    wD()
    checkAllFileNames()
    # l = ["Yellow Greafdsfen blue"]
    # check = checkFileName(l)
    # print(check)


accepter()
