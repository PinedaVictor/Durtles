# 
# 
# Victor Pineda
# 

import re 
import os


print("Wassup")

currentDir = os.getcwd()
print("Current Dirctory: " + currentDir)
editDir = "{}/Background".format(currentDir)
print("Edit Dir: " + editDir)

def reNameImages():
    print("Hi from rename funciton")
    pattern = re.compile("[a-zA-Z]*-?[a-zA-Z]*[#][(\d+(?:\.\d+)?)]*[-]?.[a-zA-Z]*")
    removeUndeDash = "_*-*"

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
    editingDir = "{}/TestingImages".format(parentPath)
    print("loppSubDirs: " + editingDir)

    for subDirs, subFolderName, files in os.walk(editingDir):
        print("In my directory loop: " + str(len(subFolderName)) + "SubDirs: " + subDirs)
        for a in subFolderName:
            print("The a in whatIs: " +  a)
        for file in files:
            print("The file: " + file)
        print("--")

loopSubDirs()

def countFiles():
    print(len(os.listdir(currentDir)))


# countFiles()