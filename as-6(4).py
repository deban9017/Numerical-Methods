from demethods import euler_method_pro as eul, trapezoidal_method_pro as trapezoidal, runge_kutta_order2_pro as rk2, taylor_method_deg2_pro as taylor
from math import log, exp

def dy_a(x, y):
    return x * exp (3*x) - 2*y

def y_a_actual(x):
    return 1/5*x*exp(3*x) - 1/25*exp(3*x) + 1/25*exp(-2*x)

def d2y_a(x, y):
    return 3*x*exp(3*x) + exp(3*x) - 2*dy_a(x, y)

def dy_b(x, y):
    return 1 + (x-y)**2

def y_b_actual(x):
    return x + 1/(1-x)

def d2y_b(x, y):
    return 2 * (x-y) - 2*(x-y)* dy_b(x, y)

def dy_c(x, y):
    return 1 + y/x

def y_c_actual(x):
    return x * log(x) + 2*x

def d2y_c(x, y):
    return -y/x**2 + dy_c(x, y)

def main():
    
    # Part (a)_________________________________________________________

    t0 = 0
    y0 = 0
    h = 0.5
    target = 1.0000005

    trape_ = trapezoidal(dy_a, t0, y0, h, target, y_actual=y_a_actual, return_errors=True, return_pairs=True)
    eul_ = eul(dy_a, t0, y0, h, target, y_actual=y_a_actual, return_errors=True, return_pairs=True)
    rk2_ = rk2(dy_a, t0, y0, h, target, y_actual=y_a_actual, return_errors=True, return_pairs=True)
    taylor_ = taylor(dy_a, d2y_a, t0, y0, h, target, y_actual=y_a_actual, return_errors=True, return_pairs=True)

    print(trape_['result'], trape_['errors'][-1], trape_['pairs'][-1])
    print(eul_['result'], eul_['errors'][-1], eul_['pairs'][-1])
    print(rk2_['result'], rk2_['errors'][-1], rk2_['pairs'][-1])
    print(taylor_['result'], taylor_['errors'][-1], taylor_['pairs'][-1])

    print()

    # Part (b)_________________________________________________________

    t0 = 2
    y0 = 1
    h = 0.5
    target = 3.000005

    trape_ = trapezoidal(dy_b, t0, y0, h, target, y_actual=y_b_actual, return_errors=True, return_pairs=True)
    eul_ = eul(dy_b, t0, y0, h, target, y_actual=y_b_actual, return_errors=True, return_pairs=True)
    rk2_ = rk2(dy_b, t0, y0, h, target, y_actual=y_b_actual, return_errors=True, return_pairs=True)
    taylor_ = taylor(dy_b, d2y_b, t0, y0, h, target, y_actual=y_b_actual, return_errors=True, return_pairs=True)

    print(trape_['result'], trape_['errors'][-1], trape_['pairs'][-1])
    print(eul_['result'], eul_['errors'][-1], eul_['pairs'][-1])
    print(rk2_['result'], rk2_['errors'][-1], rk2_['pairs'][-1])
    print(taylor_['result'], taylor_['errors'][-1], taylor_['pairs'][-1])
    
    print()

    # Part (c)_________________________________________________________

    t0 = 1
    y0 = 2
    h = 0.25
    target = 2.00000005

    trape_ = trapezoidal(dy_c, t0, y0, h, target, y_actual=y_c_actual, return_errors=True, return_pairs=True)
    eul_ = eul(dy_c, t0, y0, h, target, y_actual=y_c_actual, return_errors=True, return_pairs=True)
    rk2_ = rk2(dy_c, t0, y0, h, target, y_actual=y_c_actual, return_errors=True, return_pairs=True)
    taylor_ = taylor(dy_c, d2y_c, t0, y0, h, target, y_actual=y_c_actual, return_errors=True, return_pairs=True)

    print(trape_['result'], trape_['errors'][-1], trape_['pairs'][-1])
    print(eul_['result'], eul_['errors'][-1], eul_['pairs'][-1])
    print(rk2_['result'], rk2_['errors'][-1], rk2_['pairs'][-1])
    print(taylor_['result'], taylor_['errors'][-1], taylor_['pairs'][-1])

    # end _____________________________________________________________

if __name__ == "__main__":
    main()