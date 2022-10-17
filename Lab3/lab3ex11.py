def orderTuples(listTuples):
    for i in range(0,len(listTuples) - 1):
        if list(listTuples[i][1])[2] > list(listTuples[i+1][1])[2]:
            listTuples[i][1].replace(listTuples[i][1], listTuples[i+1][1])
    return listTuples

if __name__ == '__main__':
    print(orderTuples([('abc', 'bcd'), ('abc', 'zza')]))