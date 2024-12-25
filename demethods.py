### Description: Contains functions for numerical methods for solving differential equations


# Euler method

def euler_method(dy, t0, y0, h, target): 
    # Basic Euler method
    # Returns list of tuples [(t, y), ...] where t is time and y is the value of the function at that time
    t = t0
    y = y0
    result = []

    while t <= target:
        y += h * dy(t, y)
        result.append((t, y))
        t += h

    return result


def euler_method_pro(dy, t0, y0, h, target,
                  y_actual= None,# supply func. for error calculation
                  return_errors=False,
                  return_avg_delta_error=False,
                  return_std_dev=False,
                  return_pairs=False):

    # Returns float if no extra, all flag set to False, default
    # Returns dict if any extra, at least one flag set to True
    # Returns {'result': float, 'errors': list, 'avg_delta_error': float, 'std_dev': float} given corresponding flags true



    errors= []
    pairs = []
    t = t0
    y = y0

    while t <= target:
        y += h * dy(t, y)

        if return_pairs:
            pairs.append((t, y))

        # Error calculation
        if return_errors:
            y_true = y_actual(t)
            error = abs(y - y_true)
            # print(f"t = {t}, y = {y}, y_true = {y_true}, error = {error}")
            errors.append(error)

        t += h

    # Avg increase in error
    if return_avg_delta_error:
        avg_delta_error = sum([errors[i] - errors[i-1] for i in range(1, len(errors))]) / len(errors)
        print(f"Avg delta error = {avg_delta_error}")
    if return_std_dev:
        std_dev = (sum([(error - sum(errors)/len(errors))**2 for error in errors]) / len(errors))**0.5
        print(f"Standard deviation = {std_dev}")

    if (not return_errors) and (not return_avg_delta_error) and (not return_std_dev):
        return y # If no extra
        
    res = {'result': y}
    if return_errors:
        res['errors'] = errors
    if return_avg_delta_error:
        res['avg_delta_error'] = avg_delta_error
    if return_std_dev:
        res['std_dev'] = std_dev
    if return_pairs:
        res['pairs'] = pairs
    return res

# Second degree Taylor method

def taylor_method_deg2(dy, d2y, t0, y0, h, target):
    # Second degree Taylor method
    # Returns list of tuples [(t, y), ...] where t is time and y is the value of the function at that time
    t = t0
    y = y0
    result = []

    while t <= target:
        y += h * dy(t, y) + (h**2/2) * d2y(t, y)
        result.append((t, y))
        t += h

    return result

def taylor_method_deg2_pro(dy, d2y, t0, y0, h, target,y_actual=None, return_errors=False, return_pairs=False):
    # Returns float if no extra, all flag set to False, default
    # Returns dict if any extra, at least one flag set to True
    # Returns {'result': float, 'errors': list} given corresponding flags true
    errors= []
    pairs = []
    t = t0
    y = y0

    while t <= target:
        y += h * dy(t, y) + (h**2/2) * d2y(t, y)

        if return_pairs:
            pairs.append((t, y))

        # Error calculation
        if return_errors:
            y_true = y_actual(t)
            error = abs(y - y_true)
            errors.append(error)

        t += h

    if not return_errors:
        return y
    
    res = {'result': y, 'errors': errors}
    if return_pairs:
        res['pairs'] = pairs
    
    return res

# Runge Kutta method

def runge_kutta_order2(dy, t0, y0, h, target):
    t = t0
    y = y0
    while t <= target:
        y += h/2 * (dy(t, y) + dy(t+h, y + h*dy(t, y)))
        t += h

    return y

def runge_kutta_order4(dy, t0, y0, h, target):
    t = t0
    y = y0
    while t <= target:
        k1 = h* dy(t, y)
        k2 = h* dy(t + h/2, y + 1/2*k1)
        k3 = h* dy(t + h/2, y + 1/2*k2)
        k4 = h* dy(t + h, y + k3)

        y += 1/6 * (k1 + 2*k2 + 2*k3 + k4)
        t += h

    return y

def runge_kutta_order2_pro(dy, t0, y0, h, target, y_actual=None, return_errors=False, return_pairs=False):
    errors = []
    pairs = []
    y = y0
    t = t0
    while t <= target:
        y += h/2 * (dy(t, y) + dy(t+h, y + h*dy(t, y)))

        if return_pairs:
            pairs.append((t, y))
        
        # error calculation
        if return_errors:
            error = abs(y - y_actual(t))
            errors.append(error)
            # print(f"t: {t}, y: {y}, error: {error}")

        t += h

    if not return_errors:
        return y

    res = {'result': y, 'errors': errors}
    if return_pairs:
        res['pairs'] = pairs

    return res

def rk4_multidim(f:list, a, y:list, h, target):

    # f is list of functions F[f1, f2, f3, ...] = [dy, d2y, d3y, ...]
    # x is initial value a
    # y is initial y-val list containing y0 and dy0; y = [y(a), y'(a), y''(a), ...]
    # h is step size
    x = a
    while x < target-h:

        #NOTE: we do (target-h) since we are calculating the next step,
        #      so we stop after calculating for target using (target-h)

        k1 = [h * func(x, y) for func in f]
        k2 = [h * func(x + h/2, [y[i] + k1[i]/2 for i in range(len(y))]) for func in f]
        k3 = [h * func(x + h/2, [y[i] + k2[i]/2 for i in range(len(y))]) for func in f]
        k4 = [h * func(x + h, [y[i] + k3[i] for i in range(len(y))]) for func in f]


        """
        if list operations were supported

        k1 = [h * f(x, y)]
        k2 = [h * f(x + h/2, y + k1/2)]
        k3 = [h * f(x + h/2, y + k2/2)]
        k4 = [h * f(x + h, y + k3)]
        """

        # y += (k1 + 2*k2 + 2*k3 + k4)/6
        # Update y element-wise
        y = [y[i] + (k1[i] + 2*k2[i] + 2*k3[i] + k4[i])/6 for i in range(len(y))]

        x += h

    return y

# Trapezoidal method


def trapezoidal_method(dy, t0, y0, h, target):
    y = y0
    t = t0
    while t <= target:
        y += h/2 * (dy(t, y) + dy(t+h, fpIter_ode(dy, t, y, h, 0.000001)))
        t += h

    return y
        


def trapezoidal_method_pro(dy, t0, y0, h, target, y_actual=None, return_errors=False, return_pairs=False, print_convergence=False, tol_fpIter=0.000001):
    errors = []
    pairs = []
    y = y0
    t = t0
    while t <= target:
        y += h/2 * (dy(t, y) + dy(t+h, fpIter_ode(dy, t, y, h, tol_fpIter, print_convergence=print_convergence)))

        if return_pairs:
            pairs.append((t, y))
        
        # error calculation
        if return_errors:
            error = abs(y - y_actual(t))
            errors.append(error)
            # print(f"t: {t}, y: {y}, error: {error}")

        t += h

    if not return_errors:
        return y

    res = {'result': y, 'errors': errors}
    if return_pairs:
        res['pairs'] = pairs
    
    return res

# ODE Fixed point iteration for Trapezoidal method

def fpIter_ode(f, t0, y0, h, tol=0.00001, print_convergence=False):
    # print("FP Iteration")
    y = y0
    t = t0
    i = 0
    y_prev = y0 + tol + 1
    while abs(y_prev - y) > tol:
        y_prev = y
        y = y0 + h/2 * (f(t, y0) + f(t+h, y))
        i += 1

    if print_convergence:
        print(y, "Converged in", i, "iterations")

    return y



# Adam Bashforth methods

def adam_bashforth_2(dy, t0, y0, y1, h, target):
    t = t0+h
    y = [y0, y1]
    res = y1
    while t <= target:
        res += h/2 * (3*dy(t, y[-1]) - dy(t-h, y[-2]))
        y.append(res)
        t += h
    return res

def adam_bashforth_3(dy, t0, y0, y1, y2, h, target):
    t = t0 + 2*h
    y = [y0, y1, y2]
    res = y2
    while t <= target:
        res += h/12 * (23*dy(t, y[-1]) - 16*dy(t-h, y[-2]) + 5*dy(t-2*h, y[-3]))
        y.append(res)
        t += h
    return res

# Adam Moulton methods

def adam_moulton_2(dy, t0, y0, y1, h, target):
    t = t0+h
    y = [y0, y1]
    res = y1
    while t <= target:
        res += h/12 * (5*dy(t+h, fpIter_ode(dy,t,y[-1],h)) + 8*dy(t, y[-1]) - dy(t-h, y[-2]))
        y.append(res)
        t += h
    return y[-1]

def adam_moulton_3(dy, t0, y0, y1, y2, h, target):
    t = t0 + 2*h
    y = [y0, y1, y2]
    res = y2
    while t <= target:
        res += h/24 * (9*dy(t+h, fpIter_ode(dy,t,y[-1],h)) + 19*dy(t, y[-1]) - 5*dy(t-h, y[-2]) + dy(t-2*h, y[-3]))
        y.append(res)
        t += h
    return y[-1]    

def adam_moulton_4(dy, t0, y0, y1, y2, y3, h, target):
    t = t0 + 3*h
    y = [y0, y1, y2, y3]
    res = y3
    while t <= target:
        res += h/720 * (251*dy(t+h, fpIter_ode(dy,t,y[-1],h)) + 646*dy(t, y[-1]) - 264*dy(t-h, y[-2]) + 106*dy(t-2*h, y[-3]) - 19*dy(t-3*h, y[-4]))
        y.append(res)
        t += h
    return y[-1]

# Predictor corrector methods

def predictor_corrector_4(dy, t0, y0, y1, y2, y3, h, target):
    t = t0 + 3*h
    y = [y0, y1, y2, y3]
    res = y3
    while t <= target:
        y_pred = y[-1] + h/24 * (55*dy(t, y[-1]) - 59*dy(t-h, y[-2]) + 37*dy(t-2*h, y[-3]) - 9*dy(t-3*h, y[-4]))
        res += h/24 * (9*dy(t+h, y_pred) + 19*dy(t, y[-1]) - 5*dy(t-h, y[-2]) + dy(t-2*h, y[-3]))
        y.append(res)
        t += h
    return y[-1]


# Matrix Solver Ax = b

# Gaussian Elimination with back substitution
def gauss_elim(matrix, blank1=None, blank2=None):
    # Blank arguments are for compatibility with other matrix solvers
    """
    Gaussian Elimination with back substitution
    
    INPUT:
    matrix: list of lists, the augmented matrix
    e.g.
       [[a11 a12 a13 b1],
        [a21 a22 a23 b2],
        [a31 a32 a33 b3]]
    """


    n = len(matrix)
    for i in range(n):
        p = i
        while matrix[p][i] == 0:
            p += 1
            if p == n:
                return "No unique solution"
        if p != i:
            matrix[i], matrix[p] = matrix[p], matrix[i]
        for j in range(i+1, n):
            m = matrix[j][i]/matrix[i][i]
            for k in range(n+1):
                matrix[j][k] -= m*matrix[i][k]
    if matrix[n-1][n-1] == 0:
        return "No unique solution"
    
    # Back substitution
    x = [0]*n
    x[n-1] = matrix[n-1][n]/matrix[n-1][n-1]
    for i in range(n-2, -1, -1):
        x[i] = matrix[i][n]
        for j in range(i+1, n):
            x[i] -= matrix[i][j]*x[j]
        x[i] /= matrix[i][i]
    return x

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
        if all(abs(x[i] - x_prev[i])/max(x) < tol for i in range(n)):
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
        if all([abs(x[i] - x_prev[i])/max(x) < tol for i in range(n)]):
            break

    # print(f"Converged in {iter} iterations")
    return x

# Finite difference method
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