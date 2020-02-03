'''Run capitalize'''


def capitalizer(str_):
    '''Return capitalized string'''

    list_ = list(str_.split())

    for i, value in enumerate(list_):
        list_[i] = value.capitalize()

    return ' '.join(list_)


def main():
    '''Runs capitalizer function with user input'''

    str_ = input("Enter the name: ")
    print(capitalizer(str_))


main()
