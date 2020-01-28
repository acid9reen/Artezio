from collections import Counter


def character_frequency(str_):
    return Counter(str_)


def main():
    str_ = input("Enter the string: ")
    print(character_frequency(str_))


main()
