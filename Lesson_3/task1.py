'''Task 1 module'''

def quad(list_):
    '''Return list of quads of the numbers from given list'''

    return [x * x for x in list_]


def even_positions_elements(list_):
    '''Rerurn list of even positions elements from given list'''

    res = []

    for i in range(1, len(list_), 2):
        res.append(list_[i])

    return res


def cube_odd_positions_even_elements(list_):
    '''Return list of cubes of the odd position even numbers from given list '''

    res = []

    for i in range(0, len(list_), 2):
        if (value := list_[i]) % 2 == 0:
            res.append(value ** 3)

    return res


def main():
    '''Run all functions from this module with user input'''

    list_ = list(map(int, input("Enter elements of the list divided by space: ").split()))
    print(quad(list_))
    print(even_positions_elements(list_))
    print(cube_odd_positions_even_elements(list_))


main()
