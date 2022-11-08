def f9(pairs):
    result = []
    for num1, num2 in pairs:
        dictionary = {"sum": num1 + num2, "prod": num1 * num2, "pow": pow(num1, num2)}
        result.append(dictionary)
    return result

if __name__ == '__main__':
    print(f9([(5, 2), (19, 1), (30, 6), (2, 2)]))