from process_ex7 import process
def sum_digits(x):
    return sum(map(int, str(x)))

if __name__ == '__main__':
    print(process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], limit = 2, offset = 2))