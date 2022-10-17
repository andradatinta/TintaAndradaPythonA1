def replaceMainDiagonal(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i == j:
                matrix[i][j] = 0
    return matrix


if __name__ == '__main__':
    matrix = [[1,2,3], [4,5,6],[7,8,9]]
    print(replaceMainDiagonal(matrix))


