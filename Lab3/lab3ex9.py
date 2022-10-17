def cantSee(people):
    result = []
    numberOfColumns = len(people[0])
    for j in range(0, numberOfColumns):
        tallest = 0
        index = 0
        for i in range(0, len(people)):
            if people[i][j] > tallest:
                tallest = people[i][j]
                index = i
            elif i > index:
                result.append((i, j))
    return result

if __name__ == '__main__':
    print(cantSee([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]))