# Newton's method
# Secant method
# False position method

from math import  e as e
from math import log as log
import num_methods as method

def f(x):
    return 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9
def df(x):
    return 920*x**3 + 54*x**2 + 18*x - 221


def main():
    tol = 1e-6
    N0 = 100


    # newton raphson_____________________________________________________
    # for [0,1]
    p0 = 1 # 0.5 guess results in same answer as that of [-1,0]
    p = method.newton_raphson(p0, tol, N0, f, df)
    print('Newton method on [0,1] ',p)
    # for [-1,0]
    p0 = -0.5
    p = method.newton_raphson(p0, tol, N0, f, df)
    print('Newton method on [-1,0] ',p)

    # secant_____________________________________________________________
    # for [-1,0]
    p0 = -1
    p1 = 0
    p = method.secant(p0, p1, tol, N0, f)
    print('Secant method on [-1,0] ',p)
    # for [0,1]
    p0 = 0
    p1 = 1
    p = method.secant(p0, p1, tol, N0, f)
    print('Secant method on [0,1] ',p)

    # false position______________________________________________________
    # for [-1,0]
    p0 = -1
    p1 = 0
    p = method.false_position(p0, p1, tol, N0, f)
    print('False position method on [-1,0] ',p)
    # for [0,1]
    p0 = 0
    p1 = 1
    p = method.false_position(p0, p1, tol, N0, f)
    print('False position method on [0,1] ',p)

main()