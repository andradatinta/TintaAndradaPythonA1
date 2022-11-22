import re

def is_valid_cnp(cnp):
    if re.match('^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$', cnp):
        return True
    return False

if __name__ == '__main__':
    print(is_valid_cnp('2981211412598'))