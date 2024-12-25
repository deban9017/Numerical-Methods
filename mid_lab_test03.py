# Composite Simpsons rule
from math import e

def integration_simpson_rule(f, a, b):
    return (b-a)/6 * (f(a)+f(b)+4*f((a+b)/2))

def integration_composite_simpson_rule_modified(f, a, b, n, tol):
    n=1
    while (1):
        h = (b-a)/n
        sum = 0
        for i in range(0, n):
            sum = sum + integration_simpson_rule(f, a+(i)*h, a+(i+1)*h)

        if abs(sum - e) < tol:
            return (sum, n)
        n+=1

def f(x):
    return e**x+3*x**2

def main():
    a = 0
    b = 1
    n = 10
    tol = 1e-10
    result = integration_composite_simpson_rule_modified(f, a, b, n, tol)
    print("Composite simpson's :",result[0], "with n =", result[1])

main()