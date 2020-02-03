'''Find difference between two lists'''


def get_diff(list_1, list_2):
    '''Return list that contain difference between two given ones'''

    return list(set(list_1).symmetric_difference(set(list_2)))


def main():
    '''Run get_diff function with user input'''

    list_1 = input("Enter the 1st list: ").split()
    list_2 = input("Enter the 2nd list: ").split()

    print(get_diff(list_1, list_2))


main()
