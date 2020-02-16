'''Time_methods decorator'''

import time


def time_this(func):
    '''Function decorator for time calculation'''

    def wrapper(*args, **kwargs):

        if args and kwargs:
            time_1 = time.time()
            func(args, kwargs)
            time_2 = int((time.time() - time_1) * 1000)
        else:
            time_1 = time.time()
            func()
            time_2 = int((time.time() - time_1) * 1000)

        print(f"'{func.__name__}' method running time: {time_2} ms")

    return wrapper


def time_methods(*methods):
    '''Take decorator arguments'''

    def decorator(cls):
        '''Ckass decorator that calculate
            given method's running time'''

        class WrapperClass:
            '''Wrapper class'''

            def __init__(self, *args, **kwargs):
                self.o_instance = cls(*args, **kwargs)

            def __getattr__(self, item):
                attribute = self.o_instance.__getattribute__(item)

                if attribute.__name__ in methods:
                    return time_this(attribute)

                return attribute

        return WrapperClass

    return decorator


@time_methods('inspect', 'bar')
class Spam:
    '''Some class'''

    def __init__(self, sec):
        self.sec = sec

    def inspect(self):
        '''Some method'''

        time.sleep(self.sec)

    def some_method(self):
        '''Another some method'''

        return self.sec


def main():
    '''Create class object
        and calls it's methods'''

    obj = Spam(3)
    obj.some_method()
    obj.inspect()


if __name__ == '__main__':
    main()
