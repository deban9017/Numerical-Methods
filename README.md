This repo has my solutions to the assignments of UMC 202. The assignment pdfs are given in the corresponding folder. 

### Naming Scheme:
Any assignment solution has name `as-<assignment_number>(<question_number>).py`. For example, `as-1(1).py` is the solution to the first question of the first assignment. Lab test solutions are named accordingly. 

## USEFUL FILES:
- File `demethods.py` contain differential equation solving methods.
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



- File `Gaussian.py` contain Gauss quadrature method. I could not do it in a good way.
(TODO: Do it in a good way)
- File `num_methods.py` contains all other numerical method functions.
(TODO: Add names of functions and their descriptions)
[ignore try.py file]