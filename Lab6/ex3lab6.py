import re

def extract_list(regex_list, text):
    found = []
    for regex in regex_list:
        found += re.findall(regex, text)
    return found

if __name__ == '__main__':
    print(extract_list(['\w+', '\d+'], 'Hello, world! 123'))