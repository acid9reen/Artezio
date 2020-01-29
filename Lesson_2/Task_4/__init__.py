def range_(*args):
    step = 1
    list_ = []

    n = len(args)

    if n not in [1, 2, 3]:
        raise TypeError("range_() requires 1-3 int arguments")
    elif n == 1 or n == 2:
        stop = args[0] if n == 1 else args[1]
        start = 0 if n == 1 else args[0]

        while start < stop:
            list_.append(start)
            start += step

        return list_

    elif n == 3:
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
