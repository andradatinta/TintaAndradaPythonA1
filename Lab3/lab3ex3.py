def operations(firstList, secondList):

    intersection = list(set(firstList).intersection(secondList))
    union = list(set(firstList).union(secondList))
    differenceFirstSecond = list(set(firstList).difference(secondList))
    differenceSecondFirst = list(set(secondList).difference(firstList))

    result = [intersection, union,differenceFirstSecond,differenceSecondFirst]
    return result



if __name__ == '__main__':
    print(operations([1,4,5,9], [2,4,5,8,10]))


