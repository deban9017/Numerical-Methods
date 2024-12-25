# Newton Shooting Method / Nonlinear Shooting Method
from math import inf
from demethods import rk4_multidim as rk

def d2y(x,y,dy):
    return 1/8 * (32 +2*x**2 - y*dy)
def dy(x,y,_dy):
    return _dy

def newton_shooting(x,y,beta, b, h, tol, t0):
    t = t0
    t_prev = inf
    # we predict t, which we then use as y'(a) = t and solve the IVP
    while abs(t_prev - t)>tol:
        t_prev = t
        y_b_t_prev = rk([dy, d2y], b, [0, t_prev], h, b)


        t = t - (y_b_t_prev - beta)/ z_b_t_prev
        
