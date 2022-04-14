# 
# Victor Pineda
# Description: Goes through files in the layers directory
# and checks for spelling errors for file names.

import os
import re
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
    "correct" : False
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
    print("Chexcking all files name")
    for fileData in i:
        find_file_name = pattern.findall(fileData["name"])
        name = ''.join(find_file_name)
        # checkFileName(name)
        full_name = name.split()
        print(full_name)


def checkFileName(file_name):
    print(file_name)
    n = ''.join(file_name)
    fn = n.split()
    print(fn)
    for w in fn:
        check_word = Word(w)
        possible_corrections = check_word.spellcheck()
        file_name_correct = True
        # print(possible_corrections)
        # print(str(len(possible_corrections)))
        # print(possible_corrections[0][1] == 0.0)
        if(len(possible_corrections) == 1 and possible_corrections[0][1] == 0.0):
            print("Unkown Word 🧐")
            file_name_correct = False
        else:
            for word in possible_corrections:
                print(possible_corrections)
                if(word[0] == w):
                    print("Looks good: ✅")
                    print(w + " : " +  word[0])
                    print(file_name_correct)
        # TODO: Going to need to add truth values to a set or list
        #       and final loop to see if there are any False 
        #       values. If there are False values, there is spelling errors

        # return file_name_correct
        print("END loop")
    print("____")

wD()
# checkAllFileNames()

l = ["Yellow Grzlcihaseen blue"]
check = checkFileName(l)
print(check)

def accepter():
    print("Running")
    # runSpellChecker()

# checkAllFileNames()
# accepter()