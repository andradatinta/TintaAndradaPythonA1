def checkPalindrome(n):
    check = 0
    n1 = n
    while (n1 > 0):
        lastDigit = n1%10
        check = check*10 + lastDigit
        n1 = n1//10
        print(n % 10)
        print(check)
    if(n == check):
        print("The number %d is a palindrome" % n)
    else:
        print("The number %d is NOT a palindrome" % n)

if __name__ == '__main__':
    checkPalindrome(1221)