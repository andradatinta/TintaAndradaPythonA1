def build_xml_element(tag, content, *attributes):
    toBeBuilt = "<" + tag + ' '
    endingTag= "</" + tag + '>'
    for attribute in attributes:
        for key in attribute.keys():
            toBeBuilt += key
            toBeBuilt += ':'
        for value in attribute.values():
            toBeBuilt += value
    toBeBuilt = toBeBuilt + '>' + content + endingTag
    return toBeBuilt

if __name__ == '__main__':
    print(build_xml_element("a", "Hello there", dict(href =" http://python.org "), dict(_class =" my-link "), dict(id= " someid ")))
