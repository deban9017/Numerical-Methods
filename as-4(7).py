#FOLLOWING CODE NOT WORKING#####################################################  


# two variable integration using gauss quadrature 

import num_methods as nm
from math import log

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
    integral = gauss_quadrature(
        f = lambda x: gauss_quadrature(
            f = lambda y: log(x+2*y),
            a = 1.0,
            b = 1.5,
            n = 2,
            root_list = nm.legendre_polynomials_roots[str(2)]
        ),
        a = 1.4,
        b = 2.0,
        n = 4,
        root_list = nm.legendre_polynomials_roots[str(4)]
    )
    print(integral)

main()