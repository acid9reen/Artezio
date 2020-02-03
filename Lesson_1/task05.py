'''Check if 3rd set is a subset of 1st and 2nd'''


def subset_of_two(set_1, set_2, set_3):
    '''Return true if 3rd set is a subset of 1st and 2nd and false in other cases'''

    return set_3.issubset(set_1) and set_3.issubset(set_2)


def main():
    '''Run subset_of_two function with user input'''

    set_1 = set(map(int, input("Enter the 1st set: ").split()))
    set_2 = set(map(int, input("Enter the 2nd set: ").split()))
    set_3 = set(map(int, input("Enter the 3rd set: ").split()))

    print(subset_of_two(set_1, set_2, set_3))


main()
