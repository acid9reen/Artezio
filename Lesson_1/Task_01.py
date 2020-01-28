def capitalizer(str_):
    list_ = list(str_.split())

    for i in range(len(list_)):
        list_[i] = list_[i].capitalize()

    return ' '.join(list_)


def main():
    str_ = input("Enter the name: ")
    print(capitalizer(str_))


main()
