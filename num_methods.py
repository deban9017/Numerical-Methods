# Legendre polynomials and roots for n = 0 to 6 are given in the dictionary legendre_polynomials_roots.
legendre_polynomials_roots = {
    '0': [],
    '1': [0],
    '2': [-0.5773502692, 0.5773502692],
    '3': [-0.7745966692, 0, 0.7745966692],
    '4': [-0.8611363116, -0.3399810436, 0.3399810436, 0.8611363116],
    '5': [-0.9061798459, -0.5384693101, 0, 0.5384693101, 0.9061798459],
    '6': [-0.9324695142, -0.6612093865, -0.2386191861, 0.2386191861, 0.6612093865, 0.9324695142]
}

def f_lagrange(x_i, x_list : list, x):
    prod = 1
    for i in range(len(x_list)):
        if x_list[i] != x_i:
            prod = prod * (x - x_list[i])/(x_i - x_list[i])
    return prod


def newton_raphson(p0, tol, N0, f, df):
    i=1
    while i<=N0:
        p = p0 - f(p0)/df(p0)
        if abs(p-p0)<tol:
            print("Newton Converged after", i, "iterations")
            return p
        i = i+1
        p0 = p
    return "Method failed after N0 iterations"

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

def false_position(p0, p1, tol, N0, f):
    i=1
    q0 = f(p0)
    q1 = f(p1)
    while i<=N0:
        p = p1 - q1*(p1-p0)/(q1-q0)
        if abs(p-p1)<tol:
            print("False position Converged after", i, "iterations")
            return p
        i = i+1
        q = f(p)
        if q*q1<0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q
    return "Method failed after N0 iterations"

def difference_table(x_list, y_list):
    # NOTE: This is only difference table and NOT divided difference table

    # we would be creating a list of lists for the forward difference table: [[.], [.,.], [.,.,.], [.,.,.,.], ......so on]
    difference_table = []
    # 1st elem list would be the y_list
    difference_table.append(y_list)
    while (len(difference_table[-1]) > 1):
        # for each row, we would be calculating the differences
        row = []
        for i in range(1, len(difference_table[-1])):
            k = len(difference_table)
            row.append((difference_table[-1][i] - difference_table[-1][i-1]))
        difference_table.append(row)

    return difference_table

def lagrange_interpolation(x_list: list, y_list: list, x: float) -> float:
    sum = 0
    n = len(x_list)-1
    for i in range(n+1):
        product = y_list[i]
        for j in range(n+1):
            if i!=j:
                product = product*(x-x_list[j])/(x_list[i]-x_list[j])
        sum = sum + product
    return sum

def integration_rectangle_rule(f, a, b): 
    return f(a)*(b-a)

def integration_midpoint_rule(f, a, b):
    mid = (a+b)/2
    return f(mid)*(b-a)

def integration_trapezoidal_rule(f, a, b):
    return (f(a)+f(b))*(b-a)/2
def integration_simpson_rule(f, a, b):
    return (b-a)/6 * (f(a)+f(b)+4*f((a+b)/2))

def integration_composite_trapezoidal_rule(f, a, b, n):
    h = (b-a)/n
    sum = 0
    for i in range(0, n):
        sum = sum + integration_trapezoidal_rule(f, a+(i)*h, a+(i+1)*h)
    return sum

def integration_composite_simpson_rule(f, a, b, n):
    h = (b-a)/n
    sum = 0
    for i in range(0, n):
        sum = sum + integration_simpson_rule(f, a+(i)*h, a+(i+1)*h)
    return sum

 

