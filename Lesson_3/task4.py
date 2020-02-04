'''Convert given xml string to dictionary and calculate its depth'''

from xml.etree import ElementTree as ET


def dict_depth(dict_):
    '''Return depth of given dictionary'''

    max_level = 0
    level = 0

    for i in str(dict_):
        if i == '{':
            level += 1
        elif i == '}':
            max_level = level if level > max_level else max_level
            level = 0

    return max_level


def tree_to_dict(tree):
    '''Convert given eTree object to dict and return it'''

    dict_ = {'name': tree.tag, 'children': []}

    if children := list(tree):
        for child in map(tree_to_dict, children):
            dict_['children'].append(child)

    return dict_


def xml_string_to_dict(str_):
    '''Run tree_to_dict() and dict_depth() functions with given xml string'''

    dict_ = tree_to_dict(ET.XML(str_))
    return dict_, dict_depth(dict_)


def main():
    '''Run xml_string_to_dict() function'''

    str_ = "<root><element1 /><element2 /><element3><element4 /></element3></root>"
    print(xml_string_to_dict(str_))


if __name__ == '__main__':
    main()
