
a,b = float(input("Введите 1-число: ")),float(input("Введите 2-число: "))
if a < b:
    print(a + b
else:
    print(a - b)
from math import *

def y(x=float):
    if x < 2:
        return((6 * sin(x) - x**2)/3)
    elif x >= 2 and x < 4:
        return((exp(1)**(3 * x - cos(2*x)))/(3 + 4 * x **6))
    else:
        return((6 * x ** 3 - 4 * tan(x + 1))**(1/5))
print(y(1))
print(y(3))
print(y(5))
