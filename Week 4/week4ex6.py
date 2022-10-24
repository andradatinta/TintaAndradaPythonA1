def tupleFunction(list):
    # duplicateElements = len(list) - len(set(list))
    duplicateDict = {element:list.count(element) for element in set(list) if list.count(element) > 1}
    duplicateElements = len(duplicateDict)
    uniqueElements = len(set(list)) - duplicateElements
    return uniqueElements, duplicateElements
if __name__ == '__main__':
    print(tupleFunction([1,2,2,3,6,5,5]))
