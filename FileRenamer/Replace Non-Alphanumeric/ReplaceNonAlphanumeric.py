import os
import sys
import re

def main():
	folderToBeRenamed = sys.argv[1]

	listOfFiles = []
	for (dirPath, dirNames, fileNames) in os.walk(folderToBeRenamed):
		listOfFiles.extend(fileNames)
		break

	for fileName in listOfFiles:
		originalFileNameWithPath = folderToBeRenamed + fileName
		name, extension = os.path.splitext(fileName)
		newName = folderToBeRenamed + "/" + replaceAlphanumericWithUnderscore(name) + extension
		os.renames(originalFileNameWithPath, newName)

def replaceAlphanumericWithUnderscore(string):
	return re.sub("\W+", "_", string)

main()