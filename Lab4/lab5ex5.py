import os
def searchInTarget(target, to_search):
    fileList = []
    if os.path.isfile(target):
        f = open(target, 'r')
        lines = f.readlines()
        for row in lines:
            if row.__contains__(to_search):
                fileList.append(os.path.basename(target))
        f.close()
    elif os.path.isdir(target):
        for (root, directories, files) in os.walk(target):
            for fileName in files:
                full_fileName=os.path.join(root, fileName)
                print(full_fileName)
                if full_fileName.endswith('.txt'):
                    fdir = open(full_fileName, 'r')
                    linesdir = fdir.readlines()
                    for rowdir in linesdir:
                        if rowdir.__contains__(to_search):
                            fileList.append(os.path.basename(full_fileName))
    else:
        raise ValueError("Not a file or directory path")

    return fileList

if __name__ == '__main__':
    print(searchInTarget("C:\\Users\\Dell\\Documents\\Facultate\\AN 3\\PYTHON\\Labs\\lab5\\ex2folder", "Andrada")) # for directory
    # print(searchInTarget("C:\\Users\\Dell\\Documents\\Facultate\\AN 3\\PYTHON\\Labs\\lab5\\ex2folder\\not.txt", "Andrada")) # for file
    # print(searchInTarget("dhfkuehgk", "Andrada")) # for exception


