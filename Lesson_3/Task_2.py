from functools import reduce


def flatten(list_):
    res = []

    for item in list_:
        if isinstance(item, (list, tuple)):
            res.extend(flatten(item))
        else:
            res.append(item)

    return res


def sum_mul(*args, **kwargs):

    list_ = flatten(list(args) + list((kwargs.values())))

    for i in list_:
        if i is None:
            print("Circular reference detected...")

            return None

    sum_ = sum(list_)
    mul = reduce(lambda x, y: (x if x else 1) * (y if y else 1), list_)

    return sum_, mul


c = [5, 6, 8, [1, 2, 3, ], ]


def main():
    print(sum_mul(1, 2, [3, 4, (5, 6, 0)], a=(10, 11),
                  b=(3, 4, [5, 6, [7, 8], []])))
    print(sum_mul(c[3].append(c)))


main()
