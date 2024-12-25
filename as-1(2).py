def fixedpointiter(g,p0, tol, n0):
    i = 1
    # g = lambda x: f(x) + x
    while i <= n0:
        p = g(p0)
        # print('p =', p)
        if abs(p - p0) < tol:
            print('Fixed point is:', p)
            print('Number of iterations:', i)
            return
        i = i + 1
        p0 = p
    print('Method failed after', n0, 'iterations')
    return
        




def f(x):
    # return x**4 - 3*x**2 - 3
    return 2*x/3 + 1/x + 1/x**3

def f1(x):
    return (3*x**2 + 3)**0.25

def main():
    p0 = 1
    tol = 1e-6
    n0 = 1000
    fixedpointiter(f,p0, tol, n0)
    fixedpointiter(f1,p0, tol, n0)
    # both functions converge to the same fixed point

main()