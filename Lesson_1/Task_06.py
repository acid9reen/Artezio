def dict_gen(n):
    return {x: x*x for x in range(1, n + 1)}


def main():
    n = int(input("Enter the number: "))
    print(dict_gen(n))


main()
