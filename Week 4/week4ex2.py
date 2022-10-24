def stringDictionary(text):
    x={letter: text.count(letter) for letter in text}
    return x

if __name__ == '__main__':
    print(stringDictionary("Ana has apples"))