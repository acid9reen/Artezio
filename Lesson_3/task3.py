'''Calculate average per 4 elements and the
    max element the function've called with'''


def average(aaa, bbb, ccc, ddd, max_=[None]):
    '''Calculate average per 4 elements and the
        max element the function've called with'''

    list_ = [aaa, bbb, ccc, ddd]

    if max_[0] is None:
        max_[0] = max(list_)

    else:
        max_c = max(list_)
        max_[0] = max_[0] if max_[0] > max_c else max_c

    return sum(list_) / 4, max_[0]


def main():
    '''Run average function'''

    print(average(-3, -2, 10, 1))
    print(average(7, 8, 8, 1))


main()
