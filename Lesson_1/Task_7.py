def merge(dict_1, dict_2):
    return {**dict_1, **dict_2}


dict_1 = {'a': 11, 'b': 44, 'c': 5,   
    'd': 9, 'e': 50, 'f': 10, }

dict_2 = {'g': 7, 'h':7, } 

print(merge(dict_1, dict_2))
