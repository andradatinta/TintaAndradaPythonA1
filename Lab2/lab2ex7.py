def extractNumber(text):
    numberExtracted = ''
    for c in text:
        if (c.isdigit()):
            numberExtracted += c
    return numberExtracted

if __name__ == '__main__':
    print(extractNumber("The apple is 123 USD"))
