def pair_even_odd(numbers_list):

    result = []
    even = 0
    odd = 0

    for element in numbers_list:
        if element % 2 == 0:
            even += 1
            if len(result) < even:
                result.append([None, None])
            result[even-1][0] = element

        elif element % 2 != 0:
            odd += 1
            if len(result) < odd:
                result.append([None, None])
            result[odd-1][1] = element

    for element in result:
        insert_index = result.index(element)
        element_tuple=tuple(element)
        result.remove(element)
        result.insert(insert_index, element_tuple)

    return result

if __name__ == '__main__':
    print(pair_even_odd([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))