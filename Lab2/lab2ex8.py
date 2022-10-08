def count1InBinary(n):
    n=str(bin(int(n)))
    count=0
    for i in n:
        if i == '1':
            count += 1
    return count
if __name__ == '__main__':
    print("The binary form of the number has %d 1's" %count1InBinary(24))