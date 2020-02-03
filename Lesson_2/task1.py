'''Print quads of odd numbers in segment [0, X] and quantity of those numbers'''

from math import ceil


def quad(max_):
    '''Print quads of odd numbers in segment [0, X] and quantity of those numbers'''

    print(f"Quantity: {ceil(max_ / 2)}")

    for i in range(1, max_ + 1, 2):
        print(f"{i}: {i * i}")


def main():
    '''Run quad function with user input'''

    max_ = int(input("Enter the max number: "))
    quad(max_)


main()
