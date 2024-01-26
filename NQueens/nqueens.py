def printSolution(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q",end=" ")
            else:
                print(".",end=" ")
        print()

def isSafe(board, row, col):

    for i in range(0, col):
        if (board[row][i] == 1):
            return False
        
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):        
        if (board[i][j] == 1):
            return False
        
    for i, j in zip(range(row, len(board), 1),
                    range(col, -1, -1)):         
         if (board[i][j] == 1):
            return False
    
    return True
        
def solveNQ(board, col):
    if col >= len(board):
        return True

    for i in range(0, len(board)):
        if (isSafe(board, i, col)):
            board[i][col] = 1

            if solveNQ(board, col +1) == True:
                return True
            
            board[i][col] = 0

    return False

def main():
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             ]
 
    if solveNQ(board, 0) == False:
        print("Solution does not exist")
        return False
 
    printSolution(board)

if __name__ == "__main__":
    main()