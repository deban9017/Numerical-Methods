# Rectangle rule and Midpoint rule for integration

import num_methods as nm

def f(x):
    return (1+x**2)**(0.5)

def main():
    a=1
    b=5
    print("Rectangle rule: ", nm.integration_rectangle_rule(f, a, b))
    print("Midpoint rule: ", nm.integration_midpoint_rule(f, a, b))
    print("Trapezoidal rule: ", nm.integration_trapezoidal_rule(f, a, b))

main()