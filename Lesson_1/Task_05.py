def subset_of_two(set_1, set_2, set_3):
    return set_3.issubset(set_1) and set_3.issubset(set_2)


def main():
    set_1 = set(map(int, input("Enter the 1st set: ").split()))
    set_2 = set(map(int, input("Enter the 2nd set: ").split()))
    set_3 = set(map(int, input("Enter the 3rd set: ").split()))

    print(subset_of_two(set_1, set_2, set_3))


main()