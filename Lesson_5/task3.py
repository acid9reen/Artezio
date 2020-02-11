'''Task 3'''


class Observable:
    '''Base class'''
    @classmethod
    def __init__(cls, **kwargs):
        for (field, value) in kwargs.items():
            setattr(cls, field, value)

    def __str__(self):
        attributes = [attr for attr in dir(self)
                      if not attr.startswith('__')]
        return str(attributes)


class XXX(Observable):
    '''Empty class'''

    pass


def main():
    '''Create an object with user attributes'''

    xxx = XXX(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
    print(xxx)


if __name__ == '__main__':
    main()
