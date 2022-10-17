def countPalindrome(numbers):
    count = 0
    greatest = 0
    for i in range(0, len(numbers)):
        palindrome = 0
        number = numbers[i]
        while(number > 0 ):
            palindrome = palindrome * 10 + number%10
            print(palindrome)
            print(number%10)
            number = number//10
        if(palindrome == numbers[i]):
            count += 1
            if(palindrome > greatest):
                greatest = palindrome
    return count, greatest

if __name__ == '__main__':
    print(countPalindrome([123, 101, 3456, 2222, 444, 11, 23]))