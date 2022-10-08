import sys

def computeGCD(x, y):
    while (y):
        x, y = y, x % y
    return abs(x)

if __name__ == '__main__':
    print(computeGCD(int(sys.argv[1]), int(sys.argv[2])))