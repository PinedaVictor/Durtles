# 
# 
# Victor Pineda
# 

import re 
import os


# print("Wassup")

currentDir = os.getcwd()
# print("Current Dirctory: " + currentDir)
editDir = "{}/Background".format(currentDir)
# print("Edit Dir: " + editDir)

pattern = re.compile("[a-zA-Z]* ?-?[a-zA-Z]* ?-?[\s]?[a-zA-Z]*[#][(\d+(?:\.\d+)?)]*[-]?.[a-zA-Z]*")
removeUndeDash = "_*-*"

def reNameImages():
    print("Hi from rename funciton")

    for filename in os.listdir(editDir):
        # print("File Name: " + filename)
        src = "{0}/{1}".format(editDir, filename)
        findPattern = pattern.findall(filename)
        tempName = ''.join(findPattern)
        newName = re.sub(removeUndeDash, '', tempName)
        print("New name: " + newName)
        dist = "{0}/{1}".format(editDir, newName)
        # print(dist)
        os.rename(src, dist)
        

# reNameImages()


def loopSubDirs():
    print("In loopSubDirs")
    parentPath = os.path.dirname(currentDir)
    print("Parent Dir: " + parentPath)
    editingDir = "{}/Layers".format(parentPath)
    print("loppSubDirs: " + editingDir)

    for subDir, subFolderName, files in os.walk(editingDir):
        print("In my directory loop: " + str(len(subFolderName)) + " SubDirs: " + subDir)
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

loopSubDirs()

def countFiles():
    print(len(os.listdir(currentDir)))


# countFiles()