from math import sqrt

def isPrime(numbers):
    primeNumbers = []
    for index, number in enumerate(numbers):
        check = 0
        for d in range(2, int(sqrt(number)) + 1):
            if (number % d == 0):
                check = 1
                break
        if (check == 0):
            primeNumbers.append(number)
    return primeNumbers

if __name__ == '__main__':
    numbers = [8, 2, 17, 3, 4, 22, 61]
    primeNumbers = isPrime(numbers)
    print(primeNumbers)

