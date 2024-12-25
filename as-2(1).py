# Newton Raphson method
from math import  e as e
from math import log as log

def f_1(x):
    return x**3 - 2*x**2-5

def df_1(x):
    return 3*x**2 - 4*x

def f_2(x):
    return x**2 - 2*x*e**(-x) + e**(-2*x)

def df_2(x):
    return 2*x + 2*x*e**(-x) - 2*e**(-x) - 2*e**(-2*x)

def f_3(x):
    return (x-2**(-x))**3

def df_3(x):
    return 3*(x-2**(-x))**2*(1+2**(-x)*log(2))

def newton_raphson(p0, tol, N0, f, df):
    i=1
    while i<=N0:
        p = p0 - f(p0)/df(p0)
        if abs(p-p0)<tol:
            print("Converged after", i, "iterations")
            return p
        i = i+1
        p0 = p
    return "Method failed after N0 iterations"

def main():
    p0 = 2.5
    tol = 1e-5
    N0 = 100
    p = newton_raphson(p0, tol, N0, f_1, df_1)
    print('(Q1) ',p)
    p0 = 0.5
    p = newton_raphson(p0, tol, N0, f_2, df_2)
    print('(Q2) ',p)
    p0 = 0.5
    p = newton_raphson(p0, tol, N0, f_3, df_3)
    print('(Q3) ',p)


main()