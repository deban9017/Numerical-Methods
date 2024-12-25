from math import exp
import demethods as de

def dy(t,y):
    return t*exp(3*t) - 2*y


def y_actual(t):
    return (1/5)*t*exp(3*t) - (1/25)*exp(3*t) + (1/25)*exp(-2*t)


def main():
    y0 = 0
    h = 0.05
    t0 = 0
    target = 1
    y = de.euler_method_pro(dy, t0, y0, h, target, y_actual= y_actual, return_errors=True, return_avg_delta_error=True)

    print(f"y({target}) = {y['result']}")
    print(f"y_actual({target}) = {y_actual(target)}")
    print(f"Error = {abs(y['result'] - y_actual(target))}")

if __name__ == "__main__":
    main()