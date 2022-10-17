def countInLists(*lists, x):
    numbers = []
    concatList = []
    for list in lists:
        concatList = concatList + list
    for i in range(0, len(concatList)):
        if concatList.count(concatList[i]) == x and concatList[i] not in numbers:
            numbers.append(concatList[i])
    return numbers

if __name__ == '__main__':
    print(countInLists([1,2,3], [2,3,4], [4,5,6], [4, 1,"test"], x=2))


