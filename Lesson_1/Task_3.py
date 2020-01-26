def start_end(str_):
    return str_[:2] + str_[-2:] if len(str_) > 1 else "Empty String"


str_ = input("Enter the string: ")
print(start_end(str_))
