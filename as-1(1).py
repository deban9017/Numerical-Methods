def bisection(f,a,b,tol,n0):
    i=1
    FA = f(a)
    while i<=n0:
        p = a + (b-a)/2
        FP = f(p)
        if FP == 0 or (b-a)/2 < tol:
            print('Root is:',p)
            print('Number of iterations:',i)
            return
        i = i+1
        if FA*FP > 0:
            a = p
            FA = FP
        else:
            b = p
    print('Method failed after',n0,'iterations')
    return





def fu(x):
    return x**3 - 7*x**2 + 14*x - 6



def main():
    b=4
    a=3.2
    tol = 1e-4
    n0 = 1000
    bisection(fu,a,b,tol,n0)

main()