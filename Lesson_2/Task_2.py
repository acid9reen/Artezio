def devident_counter(a, b, c):
    i = a + 1
   
    while (i % c != 0):
        i += 1
        if (i > b):
            return 0

    return (b - i + 1) // c

a, b, c = map(int, input("Enter 3 numbers: ").split())
print(devident_counter(a, b, c))
