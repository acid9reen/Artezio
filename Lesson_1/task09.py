'''Remove duplicates from the given list'''


def delete_duplicates(list_):
    '''Return list without duplicates'''

    return list(set(list_))


def main():
    '''Run delete_duplicates function with user input'''

    list_ = input("Enter the list: ").split()
    print(f"{delete_duplicates(list_)}")


main()
