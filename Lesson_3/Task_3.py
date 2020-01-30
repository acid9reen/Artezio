g_a = None


def average(a, b, c, d):
    list_ = [a, b, c, d]
    global g_a

    if g_a is None:
        g_a = max(list_)
    else:
        g_a = g_a if g_a > (max_ := max(list_)) else max_

    return sum(list_) / 4, g_a


def main():
    print(average(-3, -2, 10, 1))
    print(average(7, 8, 8, 1))


main()
