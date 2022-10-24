from deepdiff import DeepDiff
def checkIfDictsEqual(dict1, dict2):
    check = DeepDiff(dict1, dict2)
    if check:
        return False
    else:
        return True
if __name__ == '__main__':
    print(checkIfDictsEqual({'apple': 4, 'orange': 3, 'banana': [3, 7, 5]}, {'apple': 2, 'orange': 3, 'banana': [3, 2, 2]}))