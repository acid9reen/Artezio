'''Make a string made of the first 2 and the last 2 chars from a given a string'''


def start_end(str_):
    '''Return a string made of the first 2 and the last 2 chars from a given a string'''

    return str_[:2] + str_[-2:] if len(str_) > 1 else "Empty String"


def main():
    '''Run start_end function with user input'''

    str_ = input("Enter the string: ")
    print(start_end(str_))


main()
