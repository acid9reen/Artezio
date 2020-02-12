'''Generator that return cyclic iterator'''


def cycle(list_=('a', 'b', 'c')):
    '''Generator that return cyclic iterator'''

    while True:
        for item in list_:
            yield item


def main():
    '''Create cycle() generator and
        call next() function for four times'''

    i = 0
    list_ = [1, 2, 3, 4, 5]
    obj = cycle(list_)

    while i < 7:
        print(next(obj))
        i += 1


if __name__ == '__main__':
    main()
