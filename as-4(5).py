from math import sin, cos, pi
import num_methods as nm
import numpy as np

def f(x):
    return x**2 *  sin(x)

def gauss_quadrature(f,a,b,n,root_list : list):
    sum = 0
    for i in range(n):
        #print(root_list[i])
        x = root_list[i]
        f_lagrangian_value = 0
        f_lagrangian_value = nm.integration_composite_simpson_rule(lambda y: nm.f_lagrange(x, root_list, y), a, b, 1000)
        sum = sum + f_lagrangian_value*f(x)
    return sum 

def main():
    a = 0
    b = pi/4
    n = 2 # changed from 1 to 2 #only difference with as-4(4).py
    print(gauss_quadrature(f, a, b, n, nm.legendre_polynomials_roots[str(n)]))

main()