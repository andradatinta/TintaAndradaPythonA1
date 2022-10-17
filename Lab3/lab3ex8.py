def asciiCodes(x, listOfStrings, flag):
    finalList = []
    for i in range(0, len(listOfStrings)):
        divLetters = []
        for letter in listOfStrings[i]:
            if(flag == True):
                if (ord(letter) % x == 0):
                    divLetters.append(letter)
            else:
                if (ord(letter) % x != 0):
                    divLetters.append(letter)
        finalList.append(divLetters)
    return finalList

if __name__ == '__main__':
    print(asciiCodes(2,  ["test", "hello", "lab002"], flag=False))