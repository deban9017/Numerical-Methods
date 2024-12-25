import math

# Newton's forward difference interpolation


def newtons_forward_difference(x_list: list, y_list: list, n: int, x: float, equispaced=True ) -> float:
    h = x_list[1] - x_list[0]
    # x= x0 + sh
    s = (x - x_list[0]) / h
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

    # function value at x calculation
    result = y_list[0]
    for k in range(1, len(difference_table)):
        term = 1
        for i in range(0, k):
            print(k, i)
            term *= (x - x_list[i])/h
        term *= (difference_table[k][0])/math.factorial(k)
        result += term

    print(difference_table)
    print(result)
    return result




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
    newtons_forward_difference(x_list, y_list, n, x)



main()
