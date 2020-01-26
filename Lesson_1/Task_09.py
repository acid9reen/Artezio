def delete_dublicates(list_):
    return list(set(list_))


list_ = input("Enter the list: ").split()
print(f"{delete_dublicates(list_)}")
