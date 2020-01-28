from collections import Counter


def max_3(dict_):
    counter = Counter(dict_)
    return counter.most_common(3)


dict_ = {'a': 11, 'b': 44, 'c': 5,      # maxes = [50, 44, 11]
         'd': 9, 'e': 50, 'f': 10,
         'g': 7, 'h': 7, }

print(max_3(dict_))
