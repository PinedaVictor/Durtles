# 
# Victor Pineda
# Description: This will rename all files in the 
# Layers directory with the following pattern.

import re 
import os
import sys
import getopt

currentDir = os.getcwd()
pattern = re.compile("[a-zA-Z]* ?-?[a-zA-Z]* ?-?[\s]?[a-zA-Z]*[#][(\d+(?:\.\d+)?)]*[-]?.[a-zA-Z]*")
removeUndeDash = "_*-*"


def rename():
    parentPath = os.path.dirname(currentDir)
    print("Parent directory: " + parentPath)
    editingDir = "{}/Layers".format(parentPath)
    print("Editing Directory: " + editingDir)

    for subDir, subFolderName, files in os.walk(editingDir):
        for file in files:
            src = "{0}/{1}".format(subDir, file)
            findPattern = pattern.findall(file)
            tempName = ''.join(findPattern)
            newName = re.sub(removeUndeDash, '', tempName)
            dist = "{0}/{1}".format(subDir, newName)
            # TODO: Uncomment when ready
            # os.rename(src, dist)


def previewRenameEdit():
    print("In loopSubDirs")
    parentPath = os.path.dirname(currentDir)
    print("Parent Dir: " + parentPath)
    editingDir = "{}/Layers".format(parentPath)
    print("loppSubDirs: " + editingDir)

    for subDir, subFolderName, files in os.walk(editingDir):
        print("In my directory loop: " + subDir)
        for file in files:
            print("The file: " + file)
            src = "{0}/{1}".format(subDir, file)
            print("The src var: " + src)
            findPattern = pattern.findall(file)
            tempName = ''.join(findPattern)
            newName = re.sub(removeUndeDash, '', tempName)
            print("New name: " + newName)
            dist = "{0}/{1}".format(subDir, newName)
            print("New dist: " + dist)
            print("      ")
        print("--")


def accepter():

    argLength = len(sys.argv)

    if(argLength == 1):
        print("No args other than sript name")
        rename()
    else:
        try:
            args = str(sys.argv)
            print("Without str function: " +  sys.argv[1])
            print("the args: " + args)
            tie, idk = getopt.getopt(args, '-v -b')
            print(tie)
            print("idk "+ idk)
        except:
            print("Error occured: Make sure your input is in the correct format ")

    

accepter()