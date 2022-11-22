import re

def extract_words(text):
    return re.findall('\w+', text)

if __name__ == '__main__':
    print(extract_words("Hello, I am coding in Python!"))