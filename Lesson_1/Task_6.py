def dict_gen(n):
    return {x: x*x for x in range(1, n + 1)}


n = int(input("Enter the number: "))
print(dict_gen(n))
