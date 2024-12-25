from math import  e as e
from math import log as log
from num_methods import newton_raphson

def f(x):
    return e**x - x -1

def df(x):
    return e**x - 1

def newton_raphson_iter_count(p0, tol, N0, f, df):
    i=1
    while i<=N0:
        p = p0 - f(p0)/df(p0)
        # if abs(p-p0)<tol:
        #     print("Newton Converged after", i, "iterations")
        #     return p
        i = i+1
        p0 = p
    return p

def newton_raphson_max_iter(p0, tol, N0, f, df):
    i=1
    while i<=N0:
        p = p0 - f(p0)/df(p0)
        if abs(p-p0)<tol:
            print("Newton Converged after", i, "iterations")
            return p, i
        i = i+1
        p0 = p
    return "Method failed after N0 iterations", i

def main():
    p0 = 1
    tol = 1e-7
    N0 = 100
    p_final, max_iter = newton_raphson_max_iter(p0, tol, N0, f, df)
    print(p_final) # converges after 24 iterations
    print('max iter:',max_iter) 
    
    # record newton raphson method for 15 iterations
    p_n_2 = newton_raphson_iter_count(p0, tol, max_iter-3, f, df)
    print(p_n_2) # after 15 iterations
    p_n_1 = newton_raphson_iter_count(p0, tol, max_iter-2, f, df)
    print(p_n_1) # after 16 iterations
    p_n = newton_raphson_iter_count(p0, tol, max_iter-1, f, df)
    print(p_n) # after 17 iterations
    e_nplus1 = abs(p_final - p_n)
    e_n = abs(p_final - p_n_1)
    e_nminus1 = abs(p_final - p_n_2)
    rate = log(e_nplus1/e_n)/log(e_n/e_nminus1)
    print('rate of convergence: ',rate) 




main()

