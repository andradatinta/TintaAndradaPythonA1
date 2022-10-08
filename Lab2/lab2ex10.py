def numberOfWords(text):
    count = 0
    words = text.split(' ')
    for w in words:
        if(w.isalnum()):
            count +=1
    return count
if __name__ == '__main__':
    print(numberOfWords("I have Python exam"))