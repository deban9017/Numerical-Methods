# Linear Shooting Method
# 2nd Order ODE

from demethods import rk4_multidim as rk4
from math import exp, log, sin, cos

def y_actual(x):
    c1 = 1.13921
    c2 = -0.03921
    return c1 * x + c2/x**2 - 3/10 * sin(log(x)) - 1/10 * cos(log(x))


def d2y_1(x, y):
    dy = y[1]
    y = y[0]
    return -2/x*dy + 2/x**2 * y + sin(log(x))/x**2

def d2y_2(x, y):
    dy = y[1]
    y = y[0]
    return -2/x*dy + 2/x**2 * y

def dydx(x, y):
    return y[1]


def linear_shooting_method(f, target, h, a, alpha, b, beta):
    # f is list of functions
    # x0 = a
    # y0 = alpha = y(a)
    # another initial condition y(b) = beta
    # target is target x
    # h is step size

    # solving the ODE y'' = P(x)y' + Q(x)y + R(x), y(a) = alpha, y'(a) = 0
    # using the RK4 method
    y1 = [alpha, 0]
    f1 = [dydx, d2y_1]
    y1_result = rk4(f1, a, y1, h, target)[0]
    y1_b = rk4(f1, a, y1, h, b)[0]

    # solving the ODE y'' = P(x)y' + Q(x)y , y(a) = 0, y'(a) = 1
    # using the RK4 method
    y2 = [0, 1]
    f2 = [dydx, d2y_2]
    y2_result = rk4(f2, a, y2, h, target)[0]
    y2_b = rk4(f2, a, y2, h, b)[0]

    # linear interpolation
    y = y1_result + (beta - y1_b) / (y2_b) * (y2_result)



    # print(f"y1({target}) = {y1_result[0]}")
    # print(f"y2({target}) = {y2_result[0]}")
    # print(f"y1({b}) = {y1_b[0]}")
    # print(f"y2({b}) = {y2_b[0]}")

    return y

def main():

    a = 1
    b = 2.0000005
    alpha = 1
    beta = 2.0000005
    target = 1.4000005
    N = 10
    h = 0.1

    # y = linear_shooting_method([dydx, d2y_1], target, h, a, alpha, b, beta)
    # print(f"y({target}) = {y}")
    # print(f"y_actual({target}) = {y_actual(target)}")

    # we print for each step, starting from a to b, with step size h, and print the error
    target = a+h+ 0.0000005 # to avoid floating point error
    for _ in range(N):
        y = linear_shooting_method([dydx, d2y_1], target, h, a, alpha, b, beta)
        print(f"{round(target,2)} error: {round(abs(y - y_actual(target)), 6)}")
        target += h



if __name__ == "__main__":
    main()

    