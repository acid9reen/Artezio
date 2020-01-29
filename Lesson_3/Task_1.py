def quad(list_):
    return [x * x for x in list_]


def even_positions_elements(list_):
    res = []

    for i in range(0, len(list_), 2):
        res.append(list_[i])

    return res


def cube_odd_positions_even_elements(list_):
    res = []

    for i in range(1, len(list_), 2):
        if (value := list_[i]) % 2 == 0:
            res.append(value ** 3)

    return res


def main():
    list_ = list(map(int, input("Enter elements of the list divided by space: ").split()))
    print(quad(list_))
    print(even_positions_elements(list_))
    print(cube_odd_positions_even_elements(list_))


main()
