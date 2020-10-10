import math

# Classes: Dealing with Complex Numbers
# www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, no):
        new_real = self.real + no.real
        new_imaginary = self.imaginary + no.imaginary
        return Complex(new_real, new_imaginary)
    def __sub__(self, no):
        new_real = self.real - no.real
        new_imaginary = self.imaginary - no.imaginary
        return Complex(new_real, new_imaginary)
    def __mul__(self, no):
        new_real = (self.real * no.real) + (-1 * self.imaginary * no.imaginary)
        new_complex = (self.real * no.imaginary) + (self.imaginary * no.real)
        return Complex(new_real, new_complex)
    def __truediv__(self, no):
        divisor = no.real**2 + no.imaginary**2
        new_real = (self.real * no.real + self.imaginary * no.imaginary) / divisor
        new_complex = (self.imaginary * no.real - self.real * no.imaginary) / divisor
        return Complex(new_real, new_complex)
    def mod(self):
        new_real = (self.real**2 + self.imaginary**2)**0.5
        return Complex(new_real, 0)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')