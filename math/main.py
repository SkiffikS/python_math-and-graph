from math import e
from scipy.integrate import quad

x0 = 0.0
x1 = 1.0
hx = 0.1
t = 0

def f(t): return e ** t ** 2

while x0 < x1:

    x0 += hx
    x0 = float('{:.2f}'.format(x0))
    result = quad(f, 0, x0)
    print(f"Значення інтегралу при x({x0}) = {result[0]}. Похибка за правилом Рунге - {result[1]}")
