'''Merge two dictionaries'''


def merge(dict_1, dict_2):
    '''Return merged dicitionary'''

    return {**dict_1, **dict_2}


def main():
    '''Run merge function'''

    dict_1 = {'a': 11, 'b': 44, 'c': 5,
              'd': 9, 'e': 50, 'f': 10, }

    dict_2 = {'g': 7, 'h': 7, }

    print(merge(dict_1, dict_2))


main()
