def special_string_counter(list_):
    counter = 0

    for str_ in list_:
        if len(str_) > 1 and str_[:1] == str_[-1:]:
            counter += 1

    return counter


def main():
    list_ = input().split()
    print(special_string_counter(list_))


main()
