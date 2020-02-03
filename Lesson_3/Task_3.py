def average(a, b, c, d):
    list_ = [a, b, c, d]

    if average.max_ is None:
        average.max_ = max(list_)
    else:
        average.max_ = average.max_ if average.max_ > (max_ := max(list_)) else max_

    return sum(list_) / 4, average.max_


average.max_ = None


def main():
    print(average(-3, -2, 10, 1))
    print(average(7, 8, 8, 1))


main()
