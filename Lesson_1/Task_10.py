def get_diff(list_1, list_2):
    return list(set(list_1) - set(list_2))


list_1 = input("Enter the 1st list: ").split()
list_2 = input("Enter the 2nd list: ").split()

print(get_diff(list_1, list_2))
