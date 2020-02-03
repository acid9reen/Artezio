'''Count dividends of c in interval (a, b)'''


def dividend_counter(start, end, divisor):
    '''Return quantity of dividends of c in interval (a, b)'''

    i = start + 1

    while i % divisor != 0:
        i += 1
        if i > end:
            return 0

    return (end - i - 1) // divisor + 1


def main():
    '''Run dividend_counter function with user input'''

    start, end, divisor = map(int, input("Enter 3 numbers: ").split())
    print(dividend_counter(start, end, divisor))


main()
