'''Calculate average per 4 elements and the
    max element the function've called with'''


def average(aaa, bbb, ccc, ddd, max_m=[None]):
    '''Calculate average per 4 elements and the
        max element the function've called with'''

    list_ = [aaa, bbb, ccc, ddd]

    if max_m[0] is None:
        max_ = max(list_)
        max_m[0] = max_
    else:
        max_ = max_m[0] if max_m[0] > (max_ := max(list_)) else max_
        max_m[0] = max_

    return sum(list_) / 4, max_


def main():
    '''Run average function'''

    print(average(-3, -2, 10, 1))
    print(average(7, 8, 8, 1))


main()
