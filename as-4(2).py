import num_methods as nm
from math import e
from math import sin as sin
from math import pi as pi

def f_a(x):
    return (2/(x-4))

def f_b(x):
    return (e**(3*x))*sin(2*x)

def main():
    a_1 = 0
    b_1 = 0.5

    a_2 = 0
    b_2 = pi/4

    print("Trapezoidal rule (a): ", nm.integration_trapezoidal_rule(f_a, a_1, b_1))
    print("Simpson's rule (a): ", nm.integration_simpson_rule(f_a, a_1, b_1))
    print("Trapezoidal rule: (b)", nm.integration_trapezoidal_rule(f_b, a_2, b_2))
    print("Simpson's rule (b): ", nm.integration_simpson_rule(f_b, a_2, b_2))

main()