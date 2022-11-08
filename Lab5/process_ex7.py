def process(filters, limit, offset):
    count = 0
    fibo1 = 0
    fibo2 = 1
    fibo = []
    while count < limit + offset:
        check = 1
        for rule in filters:
            if rule(fibo1) == False:
                check = 0
        if check == 1:
            count += 1
            fibo.append(fibo1)
        n = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = n

    for i in range (0, offset):
        fibo.remove(fibo[0])
    result = []
    for i in range (0, limit):
        result.append(fibo[i])

    return result