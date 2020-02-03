'''Generate dictionary that contains a number (between 1 and n) in the form (x, x*x) '''


def dict_gen(end):
    '''Return dictionary that contains a number (between 1 and n) in the form (x, x*x) '''

    return {x: x*x for x in range(1, end + 1)}


def main():
    '''Run dict_gen function with user input'''

    end = int(input("Enter the number: "))
    print(dict_gen(end))


main()
