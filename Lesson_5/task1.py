'''Simple representation of complex number'''


import math


class Complex:
    '''Simple representation of complex number'''

    def __init__(self, realpart=0, imagpart=0):
        self.real = realpart
        self.imag = imagpart

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        realpart = ((self.real * other.real + self.imag * other.imag)
                    / (other.real ** 2 + other.imag ** 2))

        imagpart = ((self.imag * other.real - self.real * other.imag)
                    / (other.real ** 2 + other.imag ** 2))

        return Complex(realpart, imagpart)

    def __str__(self):
        return f'{self.real:.2f} - {abs(self.imag):.2f}i' \
            if self.imag < 0 \
            else f'{self.real:.2f} + {self.imag:.2f}i'

    def mod(self):
        '''Return module of complex number'''

        return f'{math.sqrt(self.real ** 2 + self.imag ** 2):.2f}'


def main():
    '''Make conversions with complex class with user input'''

    aaa, bbb = map(int, input("Enter two numbers "
                              "separated by space: ").split())
    compl1 = Complex(aaa, bbb)
    aaa, bbb = map(int, input("Enter two numbers "
                              "separated by space: ").split())
    compl2 = Complex(aaa, bbb)

    print(f"Sum: {compl1 + compl2}")
    print(f"Difference: {compl1 - compl2}")
    print(f"Product: {compl1 * compl2}")
    print(f"Quotient: {compl1 / compl2}")
    print(f"Modules: {compl1.mod()}, {compl2.mod()}")


if __name__ == '__main__':
    main()
