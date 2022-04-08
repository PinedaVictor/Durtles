# 
# Victor Pineda
# Description: List all folders in the Layers directory


import os

currentDir = os.getcwd()
parentPath = os.path.dirname(currentDir)
layersDir = "{}/Layers".format(parentPath)

def countFolders():
    print(len(os.listdir(layersDir)))

countFolders()