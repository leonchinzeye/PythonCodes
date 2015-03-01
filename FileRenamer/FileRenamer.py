import os
import sys


def main():
    checkArguments()
    performRenaming()


# Checks if the appropriate arguments are given
def checkArguments():
    if len(sys.argv) != 3:
        print "Usage: \"[python] [FileRenamer.py] [directory/that/you/want/to/rename] [new naming extension]\""
        print "Eg: python FileRenaming.py MyFolderOfFiles/Participant\ 1/ document.txt"
        exit(1)
    else:
        print "Arguments = " + str(sys.argv)


def performRenaming():
    folderToBeRenamed = sys.argv[1]
    newNaming = sys.argv[2].split(".")
    # print "Folder To Be Renamed = " + folderToBeRenamed
    print "New Name = " + str(newNaming)

    # in this for loop, os.walk() grabs all the files in the folder that user has specified in the argument
    listOfFiles = []
    for (dirpath, dirnames, fileNames) in os.walk(folderToBeRenamed):
        listOfFiles.extend(fileNames)
        break


    # This for loop performs the renaming of the files
    # listOfFiles is an array of strings
    counter = 1
    for fileName in listOfFiles:
        fileCounter = "%03d" %counter
        originalFileNameWithPath = folderToBeRenamed + fileName
        newFileName = folderToBeRenamed + newNaming[0] + str(fileCounter) + "." + newNaming[1]
        os.renames(originalFileNameWithPath, newFileName)
        counter += 1

    # for(i = 0; i < listOfFiles.size(); i++) {
    # 	fileName = listOfFiles[i];
    # }

    # number = 0
    # thisthing = "hello"

main()