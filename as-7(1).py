from demethods import adam_bashforth_2, adam_bashforth_3, runge_kutta_order4 as rk4
from math import exp

def dy(t, y):
    return y-t**2+1

def y_actual(t):
    return (t+1)**2-0.5*exp(t)
     

def main():
    t0 = 0
    y0 = 0.5
    h = 0.1
    target = 2


    y1 = rk4(dy, t0, y0, h/20, t0 + h) # determining w1 for two step adam bashforth
    # print(y1)
    # print(y_actual(t0 + h))
    y2 = rk4(dy, t0, y0, h/20, t0 + 2*h) # determining w2 for three step adam bashforth
    # print(y2)
    # print(y_actual(t0 + 2*h))

    # Two step adam bashforth_____________________________________________________

    y = adam_bashforth_2(dy, t0, y0, y1, h, target)
    print(y)
    print(y_actual(target))

    # Three step adam bashforth_____________________________________________________

    y = adam_bashforth_3(dy, t0, y0, y1, y2, h, target)
    print(y)
    print(y_actual(target))
    



if __name__ == "__main__":
    main()