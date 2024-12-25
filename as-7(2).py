from demethods import adam_moulton_2, adam_moulton_3, adam_moulton_4
from demethods import runge_kutta_order4 as rk4
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


    y1 = rk4(dy, t0, y0, h/20, t0 + h) # determining w1 for two step adam moulton
    y2 = rk4(dy, t0, y0, h/20, t0 + 2*h) # determining w2 for three step adam moulton
    y3 = rk4(dy, t0, y0, h/20, t0 + 3*h) # determining w3 for four step adam moulton

    # Two step adam moulton______________________________________________________

    y = adam_moulton_2(dy, t0, y0, y1, h, target)
    print('2-step:',y)

    # Three step adam moulton____________________________________________________

    y = adam_moulton_3(dy, t0, y0, y1, y2, h, target)
    print('3-step:',y)

    # Four step adam moulton_____________________________________________________

    y = adam_moulton_4(dy, t0, y0, y1, y2, y3, h, target)
    print('4-step:',y)

    #____________________________________________________________________________

    print("actual:",y_actual(target))


if __name__ == "__main__":
    main()