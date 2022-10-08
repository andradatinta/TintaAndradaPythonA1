def upperCamelToLower(a):
    return ''.join(['_' + c.lower() if c.isupper() else c for c in a]).lstrip('_')

if __name__ == '__main__':
    print(upperCamelToLower("FirstLabForPython"))