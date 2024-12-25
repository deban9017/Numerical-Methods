import num_methods as nm
from math import e
from math import tan
from math import pi

def f_a(x):
    return x**3 * e**x
def f_b(x):
    return tan(x)

def main():
    a_1 = -2
    b_1 = 2
    n_1 = 10000

    a_2 = 0
    b_2 = 3*pi/8
    n_2 = 8

    print("Composite Trapezoidal Rule (a):", nm.integration_composite_trapezoidal_rule(f_a, a_1, b_1, n_1))
    print("Composite Simpson Rule (a):", nm.integration_composite_simpson_rule(f_a, a_1, b_1, n_1))
    print("Composite Trapezoidal Rule (b):", nm.integration_composite_trapezoidal_rule(f_b, a_2, b_2, n_2))
    print("Composite Simpson Rule (b):", nm.integration_composite_simpson_rule(f_b, a_2, b_2, n_2))

main()