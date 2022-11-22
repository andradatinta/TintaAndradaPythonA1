import re

def substrings_regex(regex, text, x):
    found = []
    for sub in range(0, len(text) - x + 1):
        if re.match(regex + "{" + str(x) + "}", text[sub:sub + x]):
            found.append(text[sub:sub + x])
    return found

if __name__ == '__main__':
    print(substrings_regex('[A-Z]', 'Hello, I am coding in PYTHON!', 3))