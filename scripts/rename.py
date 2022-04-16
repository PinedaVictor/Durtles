#
# Victor Pineda
# Description: This will rename all files in the
# layers directory with the following pattern.
# Script parameters
#   * Empty rename all files in the directory
#   * -p list a preview of what the files will be renamed

import re
import os
import sys

currentDir = os.getcwd()
pattern = re.compile(
    "[a-zA-Z]* ?-?[a-zA-Z]* ?-?[\s]?[a-zA-Z]*[#][(\d+(?:\.\d+)?)]*[-]?.[a-zA-Z]*")
removeUndeDash = "_*-*"


def rename():
    parentPath = os.path.dirname(currentDir)
    print("Parent directory: " + parentPath)
    editingDir = "{}/Layers".format(parentPath)
    print("Editing Directory: " + editingDir)
    print(" ")

    for subDir, subFolderName, files in os.walk(editingDir):
        for file in files:
            src = "{0}/{1}".format(subDir, file)
            findPattern = pattern.findall(file)
            tempName = ''.join(findPattern)
            newName = re.sub(removeUndeDash, '', tempName)
            dist = "{0}/{1}".format(subDir, newName)
            os.rename(src, dist)


def previewRename():
    parentPath = os.path.dirname(currentDir)
    print("Parent Dir: " + parentPath)
    editingDir = "{}/Layers".format(parentPath)
    print("Editing Dir: " + editingDir)
    print(" ")

    for subDir, subFolderName, files in os.walk(editingDir):
        print("In directory: " + subDir)
        for file in files:
            print("File: " + file)
            src = "{0}/{1}".format(subDir, file)
            print("src: " + src)
            findPattern = pattern.findall(file)
            tempName = ''.join(findPattern)
            newName = re.sub(removeUndeDash, '', tempName)
            print("New Name: " + newName)
            dist = "{0}/{1}".format(subDir, newName)
            print("Dist: " + dist)
            print(" ")


def accepter():

    argLength = len(sys.argv)

    if(argLength == 1):
        rename()
    else:
        try:
            argument = str(sys.argv[1])
            if(argument == "-p"):
                print("args = -p")
                previewRename()
            else:
                print("ERROR: Argument does not exist")
                print("Either run defualt script or choose an acceptable argument")
        except:
            print("Error: Make sure your input is in the correct format ")


accepter()
