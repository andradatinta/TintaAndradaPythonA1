def process_item(x = int(input("Enter x: "))):
    check = x+1
    while True:
        prime = 1
        for i in range(2, check // 2):
            if (check % i) == 0:
                prime = 0
        if prime == 1:
            least_prime = check
            break
        check += 1

    print(f"Least prime number greater than x: {least_prime}")
    return least_prime