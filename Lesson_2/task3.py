'''Calculate factorial'''


def factorial(var):
    '''Return factorial'''

    res = 1

    for i in range(1, var + 1):
        res *= i

    return res


def main():
    '''Run factorial function with user input'''

    var = int(input("Enter the number: "))
    print(factorial(var))


main()
