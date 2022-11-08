def find_numbers(given_list):
    number_list = [x for x in given_list if type(x) is int]
    return number_list
if __name__ == '__main__':
    print(find_numbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))