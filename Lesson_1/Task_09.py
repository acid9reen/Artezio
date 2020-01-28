def delete_dublicates(list_):
    return list(set(list_))


def main():
    list_ = input("Enter the list: ").split()
    print(f"{delete_dublicates(list_)}")


main()
