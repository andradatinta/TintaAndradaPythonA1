def select_dictionaries(*args, **kwargs):
    list_of_dict = []
    for arg in args:
        if type(arg) is dict and len(arg) >=2:
            for key in arg.keys():
                if type(key) is str and len(key) > 2:
                    list_of_dict.append(arg)
                    break
    for key, value in kwargs.items():
        if type(value) is dict and len(value) >=2:
            for key in value.keys():
                if type(key) is str and len(key) > 2:
                    list_of_dict.append(value)
    return list_of_dict

if __name__ == '__main__':
    print(select_dictionaries({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5},
                              3764, dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))


