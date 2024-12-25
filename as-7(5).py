# Runge-Kutta 2nd order method for solving a system of ODEs

from math import exp, sin, cos

# y is u1 => f = u1' = u2
# y' is u2 => f = u2' = u3
# y'' is u3 -> depends on u1 and u2, gets updated using u1 and u2

def y_actual(x):
    return 1/5*exp(2*x) * (-2 *cos(x) + sin(x))

def u1(t, u2, u3):
    return 1/2 * (exp(2*t)*sin(t) + 2*u2 - u3)

def u2(t, u1, u3):
    return 1/2 * (u3 + 2*u1 - exp(2*t)*sin(t))

def u3(t, u1, u2):
    return exp(2*t)*sin(t) + 2*u2 - 2*u1

def f1(t, u1, u2):
    return u2

def f2(t, u1, u2):
    return u3(t, u1, u2)


def runge_kutta_order2_multidim(t0, w0u1, w0u2, target, h):
    t = t0
    u1_ = w0u1
    u2_ = w0u2
    # u3_ = u3(t, u1_, u2_)

    while t <= target-h:
        _u1_ = u1_ + h/2 * (f1(t, u1_, u2_) + f1(t+h, u1_ + h*f1(t, u1_, u2_),u2_+ h*f2(t, u1_, u2_)))
        _u2_ = u2_ + h/2 * (f2(t, u1_, u2_) + f2(t+h, u1_ + h*f1(t, u1_, u2_),u2_+ h*f2(t, u1_, u2_)))
        # _u3_ = u3(t, _u1_, _u2_)
        
        act = y_actual(t+h)
        print(f"t: {t+h}, y_actual: {act}, y_rk2: {_u1_}, error: {abs(act - _u1_)}")

        u1_ = _u1_
        u2_ = _u2_
        # u3_ = _u3_

        t += h

    return u1_

def runge_kutta_order4_multidim(t0, w0u1, w0u2, target, h):
    t = t0
    u1_ = w0u1
    u2_ = w0u2
    u3_ = u3(t, u1_, u2_)

    while t <= target-h:
        k1u1 = h * f1(t, u1_, u2_)
        k1u2 = h * f2(t, u1_, u2_)
        k2u1 = h * f1(t + h/2, u1_ + k1u1/2, u2_ + k1u2/2)
        k2u2 = h * f2(t + h/2, u1_ + k1u1/2, u2_ + k1u2/2)
        k3u1 = h * f1(t + h/2, u1_ + k2u1/2, u2_ + k2u2/2)
        k3u2 = h * f2(t + h/2, u1_ + k2u1/2, u2_ + k2u2/2)
        k4u1 = h * f1(t + h, u1_ + k3u1, u2_ + k3u2)
        k4u2 = h * f2(t + h, u1_ + k3u1, u2_ + k3u2)

        u1_ += 1/6 * (k1u1 + 2*k2u1 + 2*k3u1 + k4u1)
        u2_ += 1/6 * (k1u2 + 2*k2u2 + 2*k3u2 + k4u2)


        t += h

    return u1_


def main():
    t0 = 0
    w0u1 = -0.4
    w0u2 = -0.6
    target = 1
    h = 0.1

    print(runge_kutta_order2_multidim(t0, w0u1, w0u2, target, h))
    print(runge_kutta_order4_multidim(t0, w0u1, w0u2, target, h))
    print(y_actual(target))

if __name__ == "__main__":
    main()