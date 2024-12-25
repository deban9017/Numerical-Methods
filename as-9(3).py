# finite difference method

from math import log, sin, cos
from demethods import gauss_jacobi, gauss_seidel, gauss_elim
from demethods import finite_difference

def y_actual(x):
    c1 = 1.13921
    c2 = -0.03921
    return c1 * x + c2/x**2 - 3/10 * sin(log(x)) - 1/10 * cos(log(x))

def p(x):
    return -2/x
def q(x):
    return 2/x**2
def r(x):
    return sin(log(x))/x**2

def main():
    a = 1
    b = 2
    alpha = 1
    beta = 2
    N = 9
    res = finite_difference(p, q, r, a, b, alpha, beta, N, matrix_solver=gauss_elim, tol=1e-4)
    print(res)
    res_actual = [y_actual(a + i*(b-a)/(N+1)) for i in range(1, N+1)]
    print(res_actual)

if __name__ == "__main__":
    main()

