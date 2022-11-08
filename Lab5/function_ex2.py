def my_function(*args, **kwargs):
    s = 0
    for key, value in kwargs.items():
        s += value
    return s