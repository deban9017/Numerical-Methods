from demethods import predictor_corrector_4
from demethods import runge_kutta_order4 as rk4
from math import exp

def dy(t, y):
    return y - t**2 + 1

def y_actual(t):
    return (t+1)**2-0.5*exp(t)

def main():
    t0 = 0
    y0 = 0.5
    h = 0.1
    target = 2

    y1 = rk4(dy, t0, y0, h/20, t0+h)
    y2 = rk4(dy, t0, y0, h/20, t0+2*h)
    y3 = rk4(dy, t0, y0, h/20, t0+3*h)
    y4 = predictor_corrector_4(dy, t0, y0, y1, y2, y3, h, target)

    print(y4)
    print(y_actual(target))


if __name__ == "__main__":
    main()

