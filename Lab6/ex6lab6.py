import re

def censor_words(text):
    all_matches = re.findall('[aeiouAEIOU]\w*[aeiouAEIOU]', text)
    found = []
    for match in all_matches:
        check = ''
        for i in range(1, len(match)+1):
            if i % 2 == 0:
                check += match[i-1]
            else:
                check += '*'
        found.append(check)

    return re.sub('[aeiouAEIOU]\w*[aeiouAEIOU]', lambda x: found.pop(0), text)

if __name__ == '__main__':
    print(censor_words("oaie Ana mere pere iarna vara"))