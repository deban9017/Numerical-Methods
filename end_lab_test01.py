# finite difference method

from math import log, sin, cos
from demethods import gauss_jacobi, gauss_seidel, gauss_elim
# from demethods import finite_difference
a_q= 1
b_q= 2
c_q= 1
y0 = 0
y1 = 0
N = 9
tol = 1e-4
def f_r(x):
    return 0

def main():
    global y0, y1, tol

    a = 0
    b = 1
    alpha = y0
    beta = y1
    global N
    res = finite_difference(p, q, r, a, b, alpha, beta, N, matrix_solver=gauss_elim, tol= tol)
    print(res)
    res_actual = [y_actual(a + i*(b-a)/(N+1)) for i in range(1, N+1)]
    print(res_actual)

def finite_difference(p, q, r, a, b, alpha, beta, N, matrix_solver=gauss_jacobi, tol=1e-4):
    # given BVP y'' = p(x)y' + q(x)y + r(x), y(a) = alpha, y(b) = beta
    # p, q, r are functions
    # We solve the system of equations Ax = b
    # A is a tridiagonal matrix

    h = (b - a) / (N + 1)
    x = [a + i*h for i in range(1, N+1)] # x0 = a, xN+1 = b, list contains x1 to xN
    #matrix b
    b = [-h**2 * r(x[i]) for i in range(N)]
    b[0] += (1 + h * p(x[0]) / 2) * alpha
    b[-1] += (1 - h * p(x[-1]) / 2) * beta


    #matrix A
    A = [[0 for _ in range(N)] for _ in range(N)]
    #body diagonal
    for i in range(N):
        A[i][i] = 2 + h**2 * q(x[i])

    #upper diagonal
    for i in range(N-1):
        A[i][i+1] = -1 + h/2 * p(x[i])

    #lower diagonal
    for i in range(1, N):
        A[i][i-1] = -1 - h/2 * p(x[i])

    #append each ith elem of b to the ith row of A
    for i in range(N):
        A[i].append(b[i])

    initial_guess = [0 for _ in range(N)]
    #solve the system of equations
    x = matrix_solver(A, 1e-4, initial_guess)
    return x

def y_actual(x):
    c1 = 1.13921
    c2 = -0.03921
    return c1 * x + c2/x**2 - 3/10 * sin(log(x)) - 1/10 * cos(log(x))

def p(x):
    return 0
def q(x):
    global a_q, b_q, c_q
    return (b_q+c_q * x**2)/a_q
def r(x):
    return -f_r(x)


# Matrix solver functions
# Gauss Jacobi method
def gauss_jacobi(matrix, tol, initial_guess):
    n = len(matrix)
    x = initial_guess
    x_prev = x[:]
    # iter = 0
    while True:
        # iter += 1
        for i in range(n):
            sigma = 0
            for j in range(n):
                if i != j:
                    sigma += matrix[i][j] * x_prev[j]
            x[i] = (matrix[i][n] - sigma) / matrix[i][i]
        if all(abs(x[i] - x_prev[i]) < tol for i in range(n)):
            break
        x_prev = x[:]
    # print(f"Converged in {iter} iterations")
    return x  

# Gauss Seidel method
def gauss_seidel(matrix, tol, initial_guess):
    n = len(matrix)
    x = initial_guess
    x_prev = [0]*n
    # iter = 0
    while True:
        # iter += 1
        # print(x)
        x_prev = x[:]
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += matrix[i][j]*x[j]
            x[i] = (matrix[i][n] - sigma)/matrix[i][i]
        if all([abs(x[i] - x_prev[i]) < tol for i in range(n)]):
            break

    # print(f"Converged in {iter} iterations")
    return x















if __name__ == "__main__":
    main()

