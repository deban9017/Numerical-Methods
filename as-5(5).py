from math import exp, log
import demethods as de

def dy(t,y):
    return 1+ y/t


def y_actual(t):
    return t * log(t) + 2*t


def main():
    y0 = 2
    h = 0.25
    t0 = 1
    target = 2
    y = de.euler_method_pro(dy, t0, y0, h, target, y_actual= y_actual, return_errors=True, return_avg_delta_error=True)

    print(f"y({target}) = {y['result']}")
    print(f"y_actual({target}) = {y_actual(target)}")
    print(f"Error = {abs(y['result'] - y_actual(target))}")

if __name__ == "__main__":
    main()