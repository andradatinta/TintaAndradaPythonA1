# Using functions, anonymous functions, list comprehensions and filter, implement three methods
# to generate a list with all the vowels in a given string.

# method 1: using a function
def generate_vowels(given_string):
    vowels_in_string = []
    for letter in given_string:
        if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels_in_string.append(letter)
    return vowels_in_string

if __name__ == '__main__':
    print(f"Method 1 using a function: {generate_vowels('Programming in Python is fun')}") # method 1
    given_string = 'Programming in Python is fun'
    # method 2: using lambda function
    vowels_in_string = list(filter(lambda letter: letter.lower() in ['a', 'e', 'i', 'o', 'u'], given_string))
    print(f"Method 2 using annonymous function: {vowels_in_string}")
    vowels_in_string_list_comprehension = [letter for letter in given_string if letter.lower() in ['a', 'e', 'i', 'o', 'u']]
    print(f"Method 3 using list comprehension: {vowels_in_string_list_comprehension}")

