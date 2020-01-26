def capitalizer(str_):
    lst = list(str_.split())

    for i in range(len(lst)):
        lst[i] = lst[i].capitalize()

    return ' '.join(lst)


str_ = input("Enter the name: ")
print(capitalizer(str_))
