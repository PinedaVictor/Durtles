# 
# Victor Pineda
# Description: Goes through files in the layers directory
# and checks for spelling errors for file names.

# import symspellpy as spellchecker

import os
import re
from textblob import TextBlob
from textblob import Word

pattern = re.compile("[a-zA-Z]* ?[^jpg|#|\d|.]")
currentDir = os.getcwd()


def runSpellChecker():
    print("Calling spellcheck")
    parentPath = os.path.dirname(currentDir)
    print("Parent Dir: " + parentPath)
    editingDir = "{}/Layers".format(parentPath)
    print("Editing Dir: " + editingDir)
    print(" ")

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
            # dist = "{0}/{1}".format(subDir, newName)
            # print("Dist: " + dist)
        print(" ")

# spellcheck()


def recommendSpelling(inputWord):
    words = inputWord.split()
    for w in words:
        checkWord = Word(w)
        possibleCorrections = checkWord.spellcheck()
        if(len(possibleCorrections) > 1):
            print(w + "    1. " + str(possibleCorrections[0][0]) + " 2. " + str(possibleCorrections[1][0]))
        elif(len(possibleCorrections) == 1 and possibleCorrections[0][0] == w):
            print(w + "     1. Seems good")
        else:
            print(w + "   1. " + str(possibleCorrections[0][0]))


def accepter():
    print("Running")
    runSpellChecker()

accepter()