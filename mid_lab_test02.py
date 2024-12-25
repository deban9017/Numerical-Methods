# Newton Raphson on system of functions

def f(x):
    # x = (x1, x2)
    #f1 = x1**2 - x2
    #f2 = x1 - x2

    return (x[0]**2 - x[1],
             x[0] - x[1])

def inv_df(x):
    # x = (x1, x2)
    # returns the inverse of the jacobian matrix for f
    x1 = x[0]
    x2 = x[1]
    c = 1/(1-2*x1)
    return (-c, c,
            -c, c*2*x1)

def matrix_mult(A, B):
    # A is 2 x 2 matrix
    # B is 2 x 1 matrix
    # returns 2 x 1 matrix
    return (A[0]*B[0] + A[1]*B[1],
            A[2]*B[0] + A[3]*B[1])

def dist(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5



def newton_raphson(p0, tol, N0, f, inv_df):
    i=1
    while i<=N0:
        prod = matrix_mult(inv_df(p0), f(p0))
        p = (p0[0] - prod[0], p0[1] - prod[1])
        # print(p, "iteration", i)
        if abs(dist((1,1),p))<tol:
            print("Newton Converged after", i, "iterations")
            return p
        # else:
        #     print(abs(dist(p,p0)), "iteration", i)
        i = i+1
        p0 = p
    return "Method failed after N0 iterations"

def main():
    tol = 1e-10
    N0 = 100

    p0 = (10, 10)
    p = newton_raphson(p0, tol, N0, f, inv_df)
    print('Newton method ',p)

main()