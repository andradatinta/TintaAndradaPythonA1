import os
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
    print(orderByExtension("C:\\Users\\Dell\\Documents\\Facultate\\AN 3\\PYTHON\\Labs\\lab5"))

