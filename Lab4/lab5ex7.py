import os

def getFileInfo(file_path):
    fullPath = f"Full path: {os.path.abspath(file_path)}"
    fileSize=f"File size: {os.stat(file_path).st_size}"
    fileExtension=f"File extension: {(os.path.splitext(file_path))[1][1:]}"
    canRead=os.access(file_path, os.R_OK)
    canWrite=os.access(file_path, os.W_OK)
    return canRead

if __name__ == '__main__':
    print(getFileInfo("C:\\Users\\Dell\\Documents\\Facultate\\AN 3\\PYTHON\\Labs\\lab5\\forEx2.txt"))