import xml.etree.ElementTree as ET

def check_one_attribute(xml_path, attrs):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    return [element.tag for element in root.iter()
            if any([element.attrib.get(key) == value for key, value in attrs.items()])]

if __name__ == '__main__':
    print(check_one_attribute('ex4.xml', {"class": "url", "name": "url-form"}))