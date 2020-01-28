from math import ceil


def quad(max_):
    print(f"Quantity: {ceil(max_ / 2)}")
    
    for i in range(1, max_ + 1, 2):
        print(f"{i}: {i * i}")


def main():
    max_ = int(input("Enter the max number: "))
    quad(max_)


main()
