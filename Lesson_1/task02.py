'''Count character frequency'''

from collections import Counter


def character_frequency(str_):
    '''Return character frequency dictionary'''

    return Counter(str_)


def main():
    '''Run character_frequency function with user input'''

    str_ = input("Enter the string: ")
    print(character_frequency(str_))


main()
