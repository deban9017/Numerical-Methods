from math import exp, sin, cos

def du2(t, u1, u2):
    return exp(2*t)*sin(t) - 2*u1 + 2*u2

# du1 = u2 = dy
# u1 = y




u10 = -0.4
u20 = -0.6

a =0
b = 1
h = 0.1

while a <= b:
    k11 = 