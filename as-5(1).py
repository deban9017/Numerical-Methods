from math import log, exp

def f(x):
    return log(x)

def main():
    x0 = 1.8
    h1 = 0.1
    h2 = 0.05
    h3 = 0.01

    dfdx_1 = (f(x0 + h1) - f(x0)) / h1
    dfdx_2 = (f(x0 + h2) - f(x0)) / h2
    dfdx_3 = (f(x0 + h3) - f(x0)) / h3

    print(f"dfdx_1 = {dfdx_1}")
    print(f"dfdx_2 = {dfdx_2}")
    print(f"dfdx_3 = {dfdx_3}")

if __name__ == "__main__":
    main()