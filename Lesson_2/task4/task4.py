'''Implementation of the python2 range() functon'''


def range_(*args):
    '''Implementation of the python2 range() functon'''

    step = 1
    list_ = []

    if (args_len := len(args)) not in (1, 2, 3):
        raise TypeError("range_() requires 1-3 int arguments")

    elif args_len in (1, 2):
        stop = args[0] if args_len == 1 else args[1]
        start = 0 if args_len == 1 else args[0]

        while start < stop:
            list_.append(start)
            start += step

        return list_

    elif args_len == 3:
        step = args[2]

        if step == 0:
            raise ValueError("range_() step argument must not be zero")

        start = args[0]
        stop = args[1]

        if start < stop and step > 0:
            while start < stop:
                list_.append(start)
                start += step

        elif start > stop and step < 0:
            while start > stop:
                list_.append(start)
                start += step

        return list_


def main():
    '''Run range_ function'''

    print(range_(1, 10, 2))


if __name__ == '__main__':
    main()
