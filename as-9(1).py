# Gaussian Elimination with back substitution
from demethods import gauss_elim

def main():
    matrix = [[4,-1,1,8],
              [2,5,2,3],
              [1,2,4,11]]
    
    print(gauss_elim(matrix))
    
if __name__ == "__main__":
    main()