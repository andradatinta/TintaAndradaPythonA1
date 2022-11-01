import os
def writePathsInFile(directoryPath, filePath):
   fileList = os.listdir(directoryPath)
   f = open(filePath, "wt")
   for file in fileList:
       if os.path.basename(file).startswith("A"):
        pathName = directoryPath + "\\" + os.path.basename(file)
        f.write(pathName + "\n")

if __name__ == '__main__':
    writePathsInFile("C:\\Users\\Dell\\Documents\\Facultate\\AN 3\\PYTHON\\Labs\\lab5\\ex2folder",
                     "C:\\Users\\Dell\\Documents\\Facultate\\AN 3\\PYTHON\\Labs\\lab5\\forEx2.txt")

