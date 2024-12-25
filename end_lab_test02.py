# finite difference method

from math import log, sin, cos
from demethods import gauss_jacobi, gauss_seidel, gauss_elim
import matplotlib.pyplot as plt
# from demethods import finite_difference
a_q= 2
b_q= 0
c_q= 0
y0 = 0
y1 = 0
N = 99
tol = 1e-4
def f_r(x):
    global a_q, b_q, c_q
    return - a_q* 64* (2-12*x+12*x**2)+ (b_q + c_q*x**2)* 64 * x**2 * (1-x)**2

def main():
    global y0, y1, tol

    a = 0
    b = 1
    alpha = y0
    beta = y1
    global N
    # p = lambda x: 0
    res_elimin = finite_difference(p, q, r, a, b, alpha, beta, N, matrix_solver=gauss_elim, tol= tol)#[N//2 - 4 : N//2 + 5]
    res_jacobi = finite_difference(p, q, r, a, b, alpha, beta, N, matrix_solver=gauss_jacobi, tol= tol)#[N//2 - 4 : N//2 + 5]
    res_seidel = finite_difference(p, q, r, a, b, alpha, beta, N, matrix_solver=gauss_seidel, tol= tol)#[N//2 - 4 : N//2 + 5]
    # print(res_elimin)
    # print(res_jacobi)
    # print(res_seidel)
    res_actual = [y_actual(a + i*(b-a)/(N+1)) for i in range(1, N+1)]
    res_actual = res_actual#[N//2 - 4 : N//2 + 5]
    # print(res_actual)

    # plot the results
    x = [a + i*(b-a)/(N+1) for i in range(1, N+1)]
    # x = x[N//2 - 4 : N//2 + 5]
    # plt.plot(x, res_elimin, label="Gauss Elimination")
    plt.plot(x, res_jacobi, label="Gauss Jacobi")
    plt.plot(x, res_seidel, label="Gauss Seidel")
    plt.plot(x, res_elimin, label="Actual")
    plt.legend()
    plt.show()


def finite_difference(p, q, r, a, b, alpha, beta, N, matrix_solver=gauss_jacobi, tol=1e-5):
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
    # print(A)
    x = matrix_solver(A, 1e-4, initial_guess)
    return x

def y_actual(x):
    return 64* x**2 * (1-x)**2

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
    x_prev = x[:] # copy of x
    iter = 0
    while True:
        iter += 1
        for i in range(n):
            sigma = 0
            for j in range(n):
                if i != j:
                    sigma += matrix[i][j] * x_prev[j]
            x[i] = (matrix[i][n] - sigma) / matrix[i][i]
        if all(abs(x[i] - x_prev[i]) < tol for i in range(n)):
            break
        x_prev = x[:]
    print(f"Jacobi Converged in {iter} iterations")
    return x  

# Gauss Seidel method
def gauss_seidel(matrix, tol, initial_guess):
    n = len(matrix)
    x = initial_guess
    x_prev = [0]*n
    iter = 0
    while True:
        iter += 1
        # print(x)
        x_prev = x[:] # copy of x
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += matrix[i][j]*x[j]
            x[i] = (matrix[i][n] - sigma)/matrix[i][i]
        if all([abs(x[i] - x_prev[i]) < tol for i in range(n)]):
            break

    print(f"Seidel Converged in {iter} iterations")
    return x




if __name__ == "__main__":
    main()

