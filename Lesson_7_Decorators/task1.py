'''Average function time decorator'''


import time


def decorator_maker_with_arguments(calls):
    '''Pass arguments to inner decorator'''

    def average_time(func):
        '''Average function time decorator'''
        time_arr = []

        def wrapper(*args, **kwargs):
            '''Wrapper'''

            nonlocal time_arr
            time_1 = time.time()
            result = func(*args, **kwargs)
            time_2 = int((time.time() - time_1) * 1000)

            if len(time_arr) < calls:
                time_arr.append(time_2)
            else:
                time_arr = time_arr[-calls + 1:]
                time_arr.append(time_2)

            print(f'Average time: '
                  f'{int(sum(time_arr) / len(time_arr))} ms')

            return result

        return wrapper

    return average_time


@decorator_maker_with_arguments(calls=2)
def some_func(num):
    '''Do something'''

    time.sleep(num)
    return num


def main():
    '''Call decorated some_func function'''

    print(some_func(3))
    print(some_func(7))
    print(some_func(1))


if __name__ == '__main__':
    main()
