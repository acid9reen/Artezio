def character_frequency(str_):
    res = {}

    for keys in str_:
        res[keys] = res.get(keys, 0) + 1

    return res

str_ = input("Enter the string: ")
print(f"{character_frequency(str_)}")  # or use collections.Counter()
