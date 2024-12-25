This repo has my solutions to the assignments of UMC 202. The assignment pdfs are given in the corresponding folder. 

### Naming Scheme:
Any assignment solution has name `as-<assignment_number>(<question_number>).py`. For example, `as-1(1).py` is the solution to the first question of the first assignment. Lab test solutions are named accordingly. 

# USEFUL FILES:
## `demethods.py` :
### DE Methods:
1. **Euler's method**: 
    ```
    def euler_method(dy, t0, y0, h, target): 
    # Basic Euler method
    # Returns list of tuples [(t, y), ...] where t is time and y is the value of the function at that time
    ```
    More functionality:
    ```
    def euler_method_pro(dy, t0, y0, h, target,
                y_actual= None,# supply func. for error calculation
                return_errors=False,
                return_avg_delta_error=False,
                return_std_dev=False,
                return_pairs=False):

    # Returns float if no extra, all flag set to False, default
    # Returns dict if any extra, at least one flag set to True
    # Returns {'result': float, 'errors': list, 'avg_delta_error': float, 'std_dev': float} given corresponding flags true
    ```
1. **Second order Taylor's method**:
    ```
    def taylor_method_deg2(dy, d2y, t0, y0, h, target):
    # Second degree Taylor method
    # Returns list of tuples [(t, y), ...] where t is time and y is the value of the function at that time
    ```
    More functionality:
    ```
    def taylor_method_deg2_pro(dy, d2y, t0, y0, h, target,y_actual=None, return_errors=False, return_pairs=False):
    # Returns float if no extra, all flag set to False, default
    # Returns dict if any extra, at least one flag set to True
    # Returns {'result': float, 'errors': list} given corresponding flags true
    ```
1. **Runge Kutta method**:

    Order 2:
    ```
    def runge_kutta_order2(dy, t0, y0, h, target):
    ```
    More functionality:
    ```
    def runge_kutta_order2_pro(dy, t0, y0, h, target, y_actual=None, return_errors=False, return_pairs=False):
    ```
    Order 4:
    ```
    def runge_kutta_order4(dy, t0, y0, h, target):
    ```
    You can always use the following, even for one dimension:
    ```
    def rk4_multidim(f:list, a, y:list, h, target):

    # f is list of functions F[f1, f2, f3, ...] = [dy, d2y, d3y, ...]
    # x is initial value a
    # y is initial y-val list containing y0 and dy0; y = [y(a), y'(a), y''(a), ...]
    # h is step size
    ```
1. **Trapezoidal method**:
    ```
    def trapezoidal_method(dy, t0, y0, h, target):
    ```
    ```
    def trapezoidal_method_pro(dy, t0, y0, h, target, y_actual=None, return_errors=False, return_pairs=False, print_convergence=False, tol_fpIter=0.000001):

    ```
1. **ODE Fixed point iteration for Trapezoidal method**:
    ```
    def fpIter_ode(f, t0, y0, h, tol=0.00001, print_convergence=False):
    ```
1. ***Adam Bashforth methods**:

    2 Step (Explicit):
    ```
    def adam_bashforth_2(dy, t0, y0, y1, h, target):
    ```
    3 Step (Explicit):
    ```
    def adam_bashforth_3(dy, t0, y0, y1, y2, h, target):
    ```
1. **Adam Moulton methods**:
    All Adam Moulton methods are implicit methods, so `fpIter_ode` is used to solve the implicit equation.

    2 Step (implicit):
    ```
    def adam_moulton_2(dy, t0, y0, y1, h, target):
    ```
    3 Step (implicit):
    ```
    def adam_moulton_3(dy, t0, y0, y1, y2, h, target):
    ```
    4 Step (implicit):
    ```
    def adam_moulton_4(dy, t0, y0, y1, y2, y3, h, target):
    ```
1. **Predictor corrector method**:
    ```
    def predictor_corrector_4(dy, t0, y0, y1, y2, y3, h, target):
    ```
### Matrix Methods:
Matrix Solver Ax = b
In the Following methods, input matrix should be augmented matrix.
```
    """
    INPUT:
    matrix: list of lists, the augmented matrix
    e.g.
       [[a11 a12 a13 b1],
        [a21 a22 a23 b2],
        [a31 a32 a33 b3]]
    """
```
1. **Gauss Elimination**:
    ```
    def gauss_elim(matrix, blank1=None, blank2=None):
    # Blank arguments are for compatibility with other matrix solvers
    #Gaussian Elimination with back substitution

    ```
    1. **Gauss Jacobi method**:
    (Matrix should be augmented matrix)
    ```
    def gauss_jacobi(matrix, tol, initial_guess):
    ```
    1. **Gauss Seidel method**:
    ```
    def gauss_seidel(matrix, tol, initial_guess):
    ```
### Finite Difference Methods:
1. **Linear Finite Difference Method**:
    ```
    def finite_difference(p, q, r, a, b, alpha, beta, N, matrix_solver=gauss_jacobi, tol=1e-4):
    # given BVP y'' = p(x)y' + q(x)y + r(x), y(a) = alpha, y(b) = beta
    # p, q, r are functions
    # We solve the system of equations Ax = b
    # A is a tridiagonal matrix
    ```





### `num_methods.py` :
Contains all other numerical method functions.
1. **Dict: legendre_polynomials_roots** :
    ```
    legendre_polynomials_roots = {
        '0': [],
        '1': [0],
        '2': [-0.5773502692, 0.5773502692],
        ... # upto 6
    }
    ```
1. **Lagrange Polynomial Value**:
    ```
    def f_lagrange(x_i, x_list : list, x):
    ```
1. **Newton Raphson Method**:
    ```
    def newton_raphson(p0, tol, N0, f, df):
    ```
1. **Secant Method**:
    ```
    def secant(p0, p1, tol, N0, f):
    ```
1. ** Method of False Position**:
    ```
    def false_position(p0, p1, tol, N0, f):
    ```
1. **Difference Table**:
    ```
    def difference_table(x_list, y_list)->list:
    # NOTE: This is only difference table and NOT divided difference table

    # we would be creating a list of lists for the forward difference table: [[.], [.,.], [.,.,.], [.,.,.,.], ......so on]
    ```
1. **Lagrange Interpolation**:
    ```
    def lagrange_interpolation(x_list: list, y_list: list, x: float) -> float:
    ```
### Integration Methods:
1. **Rectangle Method**:
    ```
    def integration_rectangle_rule(f, a, b): 
    ```
1. **Midpoint Method**:
    ```
    def integration_midpoint_rule(f, a, b):
    ```
1. **Trapezoidal Method**:
    ```
    def integration_trapezoidal_rule(f, a, b):
    ```
1. **Composite Trapezoidal Method**:
    ```
    def integration_composite_trapezoidal_rule(f, a, b, n):
    ```
1. **Simposon's Rule**:
    ```
    def integration_simpson_rule(f, a, b):
    ```
1. **Composite Simpson's Rule**:
    ```
    def integration_composite_simpson_rule(f, a, b, n):
    ``` 

### `Gaussian.py`:
Contains Gauss quadrature method. I could not do it in a good way.
(TODO: Do it in a good way)

[ignore try.py file]