from math import sin,pi
def f(x):
    return x**2*sin(x)
def trapezoidal(a,b,f):
    return (b-a)*(f(a)+f(b))/2
def Lag(n,k,x_list,x):
    if n==0 and k==0:
        return 1
    prod = 1
    for i in range(n+1):
        if i == k:
            continue
        prod *=(x-x_list[i])/(x_list[k]-x_list[i])
    return prod
def simpsons(a,b,f):
    return (b-a)*(f(a)+f(b)+4*f((a+b)/2))/6
def Gaussian(n,f,a,b,x_list):
    integral = 0
    for i in range(n):
        integral += simpsons(a,b,lambda x : Lag(n-1,i,x_list,x))*f(x_list[i])
    return integral
print()
print("Using one point gaussian method : ",Gaussian(1,f,0,pi/4,[0]))
print("\nUsing three point gaussian method : ",Gaussian(6,f,0,pi/4,[-0.93247,-0.66121,-0.23862,0.23862,0.66121,0,93247]))
print("\nUsing two point point gaussian method : ",Gaussian(3,f,0,pi/4,[pi/16,pi/8,3*pi/16]))
print()
