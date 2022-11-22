import xml.etree.ElementTree as ET

def check_attributes(path, attrs):
    tree = ET.parse(path)
    root = tree.getroot()
    return [element.tag for element in root.iter()
            if all([element.attrib.get(key) == value for key, value in attrs.items()])]

if __name__ == '__main__':
    print(check_attributes('ex4.xml', {"class": "url", "name": "url-form", "data-id": "item"}))