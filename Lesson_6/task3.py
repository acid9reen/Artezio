'''Convert two lists into dictionary'''


def to_dict(keys, values):
    '''Convert two lists into dictionary'''

    dict_ = {}

    if (len_k := len(keys)) > (len_v := len(values)):
        for i in range(len_k):
            dict_[keys[i]] = None if i >= len_v else values[i]
    else:
        for i in range(len_k):
            dict_[keys[i]] = values[i]

    return dict_


def main():
    '''Run to_dict function with user lists'''

    keys = [1, 2, 3, 4, 5, 6, 7, ]
    values = ['a', 'b', 'c', ]

    print(to_dict(keys, values))
    print(to_dict(keys=values, values=keys))


if __name__ == '__main__':
    main()
