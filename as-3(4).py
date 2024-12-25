import num_methods as nm

# def lagrange_interpolation(x_list: list, y_list: list, x: float) -> float:
#     sum = 0
#     n = len(x_list)-1
#     for i in range(n+1):
#         product = y_list[i]
#         for j in range(n+1):
#             if i!=j:
#                 product = product*(x-x_list[j])/(x_list[i]-x_list[j])
#         sum = sum + product
#     return sum

def main():
    # f(0.1) = −0.62049958,
    #  f(0.2) = −0.28398668,
    #  f(0.3) = 0.00660095,
    #  f(0.4) = 0.24842440.
    x_list = [0.1, 0.2, 0.3, 0.4]
    y_list= [-0.62049958, -0.28398668, 0.00660095, 0.24842440]

    # f(−0.75) = −0.07181250,
    #  f(−0.5) = −0.02475,
    #  f(−0.25) = 0.3349375,
    #  f(0) = 1.101000.
    x_list = [-0.75, -0.5, -0.25, 0]
    y_list = [-0.07181250, -0.02475, 0.3349375, 1.101000]


    n = int(input("Enter degree of polynomial: "))
    x = float(input("Enter x: "))
    print(nm.lagrange_interpolation(x_list[:n+2], y_list[:n+2], x))

main()