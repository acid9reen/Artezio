'''Sequentially iterate the passed objects'''


def chain(*iterables):
    '''Sequentially iterate the passed objects'''

    for iterable in iterables:
        yield from iterable


def main():
    '''Sequentially iterate the passed
        objects from user via chain generator'''

    aaa = [1, 2, 3, 5, 6, 7, 8, ]
    bbb = [12, 3, 4556, 8888]

    for i in chain(aaa, bbb):
        print(i, end=' ')


if __name__ == '__main__':
    main()
