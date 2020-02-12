'''Generator that return cyclic iterator'''


def cycle():
    '''Generator that return cyclic iterator'''

    while True:
        for item in ['a', 'b', 'c']:
            yield item


def main():
    '''Create cycle() generator and
        call next() function for four times'''

    i = 0
    obj = cycle()

    while i < 4:
        print(next(obj))
        i += 1


if __name__ == '__main__':
    main()
