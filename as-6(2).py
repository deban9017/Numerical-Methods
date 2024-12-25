from math import log, exp
from demethods import euler_method_pro as eul, runge_kutta_order2_pro as rk2


def dy_a(x, y):
    return y/x - y**2/x**2

def y_a_actual(x):
    return x/(1+log(x))

def dy_b(x, y):
    return (y**2+y)/x

def y_b_actual(x):
    return (2*x)/(1 -2*x)

def dy_c(x, y):
    return - x*y + 4*x/y

def y_c_actual(x):
    return (4 - 3*exp(-(x**2)))**0.5

def main():

    # Part (a)_________________________________________________________

    t0 = 1
    y0 = 1
    h = 0.1
    target = 1.20000005

    print(rk2(dy_a, t0, y0, h, target, y_actual=y_a_actual, return_errors=True, return_pairs=True))
    print(eul(dy_a, t0, y0, h, target, y_actual=y_a_actual, return_errors=True))

    # Part (b)_________________________________________________________

    t0 = 1
    y0 = -2
    h = 0.5
    target = 3.00000005

    print(rk2(dy_b, t0, y0, h, target, y_actual=y_b_actual, return_errors=True))
    print(eul(dy_b, t0, y0, h, target, y_actual=y_b_actual, return_errors=True))

    # Part (c)_________________________________________________________

    t0 = 0
    y0 = 1
    h = 0.25
    target = 1.00000005

    print(rk2(dy_c, t0, y0, h, target, y_actual=y_c_actual, return_errors=True))
    print(eul(dy_c, t0, y0, h, target, y_actual=y_c_actual, return_errors=True))

    # end _____________________________________________________________


if __name__ == "__main__":
    main()