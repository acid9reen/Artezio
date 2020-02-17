'''Currying decorator'''


def curry(func):
    '''Curry given function'''

    def w_arg_1(arg_1):
        '''Curry given function'''

        def w_arg_2(arg_2):
            '''Curry given function'''

            def w_arg_3(arg_3):
                '''Curry given function'''

                def w_arg_4(arg_4):
                    '''Curry given function'''

                    return func(arg_1, arg_2, arg_3, arg_4)

                return w_arg_4

            return w_arg_3

        return w_arg_2

    return w_arg_1


@curry
def some_func(arg_1, arg_2, arg_3, arg_4):
    '''Do something'''

    return arg_1 + arg_2 + arg_3 + arg_4


def main():
    '''Call some_func function'''

    print(some_func(1)(2)(3)(4))


if __name__ == '__main__':
    main()
