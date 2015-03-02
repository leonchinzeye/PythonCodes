import os
import sys
import re


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


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]


def performRenaming():
    folderToBeRenamed = sys.argv[1]
    newNaming = sys.argv[2].split(".")

    # in this for loop, os.walk() grabs all the files in the folder that user has specified in the argument
    listOfFiles = []
    for (dirpath, dirnames, fileNames) in os.walk(folderToBeRenamed):
        listOfFiles.extend(fileNames)
        break

    listOfFiles.sort(key = natural_keys)

    # This for loop performs the renaming of the files
    # listOfFiles is an array of strings
    counter = 1
    for fileName in listOfFiles:
        fileCounter = "%03d" %counter
        originalFileNameWithPath = folderToBeRenamed + fileName
        newFileName = folderToBeRenamed + newNaming[0] + str(fileCounter) + "." + newNaming[1]
        os.renames(originalFileNameWithPath, newFileName)
        counter += 1


main()