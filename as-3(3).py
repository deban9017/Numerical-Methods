import num_methods as nm


# def difference_table(x_list, y_list):
#     # we would be creating a list of lists for the forward difference table: [[.], [.,.], [.,.,.], [.,.,.,.], ......so on]
#     difference_table = []
#     # 1st elem list would be the y_list
#     difference_table.append(y_list)
#     while (len(difference_table[-1]) > 1):
#         # for each row, we would be calculating the differences
#         row = []
#         for i in range(1, len(difference_table[-1])):
#             k = len(difference_table)
#             row.append((difference_table[-1][i] - difference_table[-1][i-1]))
#         difference_table.append(row)

#     return difference_table


def main():
    x_list = [-2,-1,0,1,2,3]
    y_list = [1,4,11,16,13,-4]
    diff_table = nm.difference_table(x_list, y_list)
    print(diff_table)

    # NOTE: The difference table can have element lists with only zeros.
    # So, once such an element comes, the later elements are also going to be zeros lists.
    # SO, interpolation can be only done upto the last non-zero element list. Say kth order difference, i.e. k+1 th element starting from 1.
    # So, we can interpolate upto kth order polynomial atmost.


    flag = 1
    while (flag):
        # check if last elem list of diff_table has only zeros
        temp = diff_table[-1]
        if not(all(i == 0 for i in temp)):
            flag = 0
        if flag==1:
            diff_table.pop()
        if not flag:
            break
    print(diff_table)
    print("The degree of the polynomial is:", len(diff_table)-1)

main()