def howManyVowels(vowels, checkString):
    count = 0
    for i in range(0,len(checkString)):
            if vowels.find(checkString[i]) != -1:
                count += 1
    return count
if __name__ == '__main__':
    vowels = "aeiouAEIOU"
    checkString = "Andrada"
    print(howManyVowels(vowels, checkString))