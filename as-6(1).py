from math import log, exp
from demethods import euler_method_pro as eul, taylor_method_deg2_pro as taylor



def dy_a(x, y):
    return y/x - y**2/x**2

def d2y_a(x, y):
    return (-y/x**2 + 2*y**2/x**3)*(1/x - 2*y/x**2)* dy_a(x, y)

def y_a_actual(x):
    return x/(1+log(x))

def dy_b(x, y):
    return (y**2+y)/x

def d2y_b(x, y):
    return (2*y + 1)/x * dy_b(x, y) - (y**2 + y)/x**2

def y_b_actual(x):
    return (2*x)/(1 -2*x)

def dy_c(x, y):
    return - x*y + 4*x/y

def d2y_c(x, y):
    return (-y + 4/y) * (-x-4*x/y**2) * dy_c(x, y)

def y_c_actual(x):
    return (4 - 3*exp(-(x**2)))**0.5

def main():

    # Part (a)_________________________________________________________

    t0 = 1
    y0 = 1
    h = 0.1
    target = 1.20000005

    print(taylor(dy_a, dy_a, t0, y0, h, target, y_actual=y_a_actual, return_errors=True))
    print(eul(dy_a, t0, y0, h, target, y_actual=y_a_actual, return_errors=True))

    # Part (b)_________________________________________________________

    t0 = 1
    y0 = -2
    h = 0.5
    target = 3.00000005

    print(taylor(dy_b, d2y_b, t0, y0, h, target, y_actual=y_b_actual, return_errors=True))
    print(eul(dy_b, t0, y0, h, target, y_actual=y_b_actual, return_errors=True))

    # Part (c)_________________________________________________________

    t0 = 0
    y0 = 1
    h = 0.25
    target = 1.00000005

    print(taylor(dy_c, d2y_c, t0, y0, h, target, y_actual=y_c_actual, return_errors=True))
    print(eul(dy_c, t0, y0, h, target, y_actual=y_c_actual, return_errors=True))

    # end _____________________________________________________________


if __name__ == "__main__":
    main()