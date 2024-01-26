import numpy as np
import random as rand

# using python native nested lists
def matrix_mult_native(m_one, m_two):
    m_one_row = len(m_one)
    m_two_col = len(m_two[0])
    
    # arithmetic, using iterative algorithm from wikipedia lol
    if len(m_one[0]) == len(m_two):
        
        # empty matrix of needed dimensions (rows from m_one, cols from m_two)
        result_matrix = [[0] * m_two_col for _ in range(m_one_row)] 
        
        for i in range(0, m_one_row):
            
            for j in range(0, m_two_col):
                cell = 0
                for k in range(0, len(m_two)):
                    cell = cell + (m_one[i][k] * m_two[k][j])
                    
                result_matrix[i][j] = cell
        return result_matrix
    
    # if m_one col length != m_two row length, raise error 
    else: 
        return ValueError
    
# randomly fill nested-list matrices 
def make_matrices(m1row, m1colm2row, m2col):
    # empty matrices 
    m_one = [[0] * m1colm2row for _ in range(m1row)] 
    m_two = [[0] * m2col for _ in range(m1colm2row)] 
    m_one = fill_matrix(m_one)
    m_two = fill_matrix(m_two)
    
    return [m_one, m_two]

def fill_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            matrix[i][j]  = rand.randrange(0, 100)
    return matrix

def main():
    m_one = [
        [2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6],
    ]
    m_two = [
        [2, 3, 4],
        [2, 3, 4],
        [2, 3, 4],
        [2, 3, 4],
        [2, 3, 4],
    ]
    
    m_one_np = np.matrix('2 3 4 5 6; 2 3 4 5 6; 2 3 4 5 6')
    m_two_np = np.matrix('2 3 4; 2 3 4; 2 3 4; 2 3 4; 2 3 4')
    #print(m_one_np)
    
    result_nat = matrix_mult_native(m_one, m_two)
    print("result of native matrix mult : ")
    print(result_nat)
    
    result_np = np.matmul(m_one_np, m_two_np)
    print("result of np matrix mult :")
    print(result_np)

if __name__ == "__main__":
    main()