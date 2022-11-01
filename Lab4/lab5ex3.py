import os
def countExtensions(my_path):
    fileList = []
    count = 0
    if os.path.isfile(my_path):
        f = open(my_path, 'r')
        f.seek(0, os.SEEK_END)
        f.seek(f.tell() - 20, os.SEEK_SET)
        content = f.read()
        return content
    elif os.path.isdir(my_path):
        for (root, directories, files) in os.walk(my_path):
            for fileName in files:
                full_fileName=os.path.join(root, fileName)
                fileTuple = os.path.splitext(full_fileName)
                if count == 0:
                    fileList.append((fileTuple[1], 1))
                    count = count + 1
                else:
                    for extension in fileList:
                        if extension[0] == fileTuple[1]:
                            extension = list(extension)
                            extension[1] = extension[1] + 1
                            print(extension[1])
                            extension = tuple(extension)
                    else:
                        fileList.append((fileTuple[1], 1))
    return fileList
if __name__ == '__main__':
    # print(countExtensions("C:\\Users\\Dell\\Documents\\Facultate\\AN 3\\PYTHON\\Labs\\lab5\\testduplicat.txt"))
    print(countExtensions("C:\\Users\\Dell\\Documents\\Facultate\\AN 3\\PYTHON\\Labs\\lab5"))

