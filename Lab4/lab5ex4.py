import os
import sys
def orderByExtension(path):
    fileList = os.listdir(path)
    extensionList = []
    for file in fileList:
        fileTuple = os.path.splitext(str(file))
        if fileTuple[1]:
            extensionList.append(fileTuple[1])
    extensionList.sort()
    extensionList = list(set(extensionList))
    return sorted(extensionList)

if __name__ == '__main__':
    pathWithSpaces = sys.argv[1:] # did this because my path had a space in it
    directoryPath = ""
    count = 0
    for part in pathWithSpaces:
        directoryPath += part
        if count == 0:
            directoryPath += ' '
        print(directoryPath)
        count += 1
    print(orderByExtension(directoryPath))



