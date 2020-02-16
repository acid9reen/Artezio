'''Annotations checker decorator'''


from math import sqrt


def annotations_checker(func):
    '''Check annotation for function'''

    def wrapper(*args):
        annotations = func.__annotations__
        keys = annotations.keys()
        varnames = func.__code__.co_varnames

        if 'return' not in keys:
            raise Exception("The annotation is incomplete")

        for i in varnames:
            if i not in keys:
                raise Exception("The annotation is incomplete")

        for index, value in enumerate(args):
            if not isinstance(value, annotations.get(varnames[index])):
                print("The  passed arguments didn't match the annotation")
                return None

        result = func(*args)

        if not isinstance(result, annotations.get('return')):
            print("The  passed arguments didn't match the annotation")

            return None

        return result

    return wrapper


@annotations_checker
def some_func(x_coor: float, y_coor: float) -> float:
    '''Calculate 2D vector's length'''

    return sqrt(x_coor ** 2 + y_coor ** 2)


def main():
    '''Call some_func function'''

    print(some_func(4.0, 3.0))


if __name__ == '__main__':
    main()
