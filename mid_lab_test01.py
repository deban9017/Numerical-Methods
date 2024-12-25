def secant(p0, p1, tol, N0, f):
    i=1
    q0 = f(p0)
    q1 = f(p1)
    while i<=N0:
        p = p1 - q1*(p1-p0)/(q1-q0)
        if abs(p-p1)<tol:
            print("Secant Converged after", i, "iterations")
            return p
        i = i+1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
    return "Method failed after N0 iterations"

def f(x):
    return x**2 - 2

def main():
    tol = 1e-6
    N0 = 100
    p0 = 5
    p1 = 6
    p = secant(p0, p1, tol, N0, f)
    print('Secant method ',p)

main()