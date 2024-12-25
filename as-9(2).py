# Gauss Jacobi Method to solve linear equations
from demethods import gauss_jacobi

def main():
    matrix = [
        [10,-1,2,0,6],
        [-1,11,-1,3,25],
        [2,-1,10,-1,-11],
        [0,3,-1,8,15]
        ]
    initial_guess = [0]*len(matrix)
    tol = 0.001
    res = gauss_jacobi(matrix, tol, initial_guess)
    print([round(result,2) for result in res])

if __name__ == "__main__":
    main()
