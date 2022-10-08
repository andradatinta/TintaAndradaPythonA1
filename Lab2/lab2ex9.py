def mostUsedLetter(text):
    minCount = 0
    for c in text:
        c=c.lower()
        if(c != ' '):
            countCharacter = text.count(c)
            if (countCharacter > minCount):
                minCount = countCharacter
                maxLetter = c
    return maxLetter

if __name__ == '__main__':
    print("The most used letter in the given text is %8s" %mostUsedLetter("An apple is not a tomato"))