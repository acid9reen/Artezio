def factorial(n):
    res = 1

    for i in range(1, n + 1):
        res *= i

    return res


def main():
    n = int(input("Enter the number: "))
    print(factorial(n))


main()
