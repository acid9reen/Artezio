'''Flatten the list or tuple'''

from functools import reduce


def flatten(list_):
    '''Flatten the list or tuple'''

    res = []

    for item in list_:
        if isinstance(item, (list, tuple)):
            res.extend(flatten(item))
        else:
            res.append(item)

    return res


def sum_pro(*args, **kwargs):
    '''Return sum and product of the all non-0 elements from given list'''

    list_ = flatten(list(args) + list((kwargs.values())))

    for i in list_:
        if i is None:
            print("Circular reference detected...")

            return None

    sum_ = sum(list_)
    product = reduce(lambda x, y: (x if x else 1) * (y if y else 1), list_)

    return sum_, product


def main():
    '''Run sum_pro function'''

    ccc = [5, 6, 8, [1, 2, 3, ], ]

    print(sum_pro(1, 2, [3, 4, (5, 6, 0)], a=(10, 11),
                  b=(3, 4, [5, 6, [7, 8], []])))
    print(sum_pro(ccc[3].append(ccc)))


main()
