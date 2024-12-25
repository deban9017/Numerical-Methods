# teo variable composite simpson's

from math import log
import num_methods as nm

def f(x):
    log(x)

def main():
    integral = nm.integration_composite_simpson_rule(
        f = lambda x: nm.integration_composite_simpson_rule(
            f=lambda y:log(x+2*y),
            a=1.0,
            b=1.5,
            n=2
            ),
        a= 1.4,
        b= 2.0,
        n=4)
    print(integral)

main()