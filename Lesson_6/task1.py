'''Even iterator'''


class EvenIterator:
    '''Even iterator'''

    index = -1

    def __init__(self, list_):
        self.list_ = [list_[x] for x in range(0, len(list_), 2)]

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1

        if self.index < len(self.list_):
            return self.list_[self.index]

        raise StopIteration


def main():
    '''Create even iterator from list and print all its elements'''

    list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    for i in EvenIterator(list_):
        print(i)


if __name__ == '__main__':
    main()
