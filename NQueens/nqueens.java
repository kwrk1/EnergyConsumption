package NQueens;

public class nqueens {
    public static void printSolution(int board[][]){
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                if (board[i][j] == 1)
                    System.out.print("Q ");
                else
                    System.out.print(". ");
            }
            System.out.println();
        }
    }

    public static boolean isSafe(int board[][], int row, int col){
        for (int i = 0; i < col; i++)
            if (board[row][i] == 1)
                return false;
 
        // Check upper diagonal on left side
        for (int i = row, int j = col; i >= 0 && j >= 0; i--, j--)
            if (board[i][j] == 1)
                return false;
 
        // Check lower diagonal on left side
        for (int i = row, int j = col; j >= 0 && i < board.length; i++, j--)
            if (board[i][j] == 1)
                return false;
 
        return true;

    }

    public static boolean solveNQ(int board[][], int col){
            if (col >= board.length)
                return true;
     
            for (int i = 0; i < board.length; i++) {
                 
                if (isSafe(board, i, col)) {  
                    board[i][col] = 1;
     
                    if (solveNQUtil(board, col + 1) == true)
                        return true;

                    board[i][col] = 0;
                }
            }

            return false;        
    }

    public static void main(String args[]){
        int board[][] = { { 0, 0, 0, 0 },
                        { 0, 0, 0, 0 },
                        { 0, 0, 0, 0 },
                        { 0, 0, 0, 0 } };
        
        if (solveNQ(board, 0) == false) {
            System.out.print("Solution does not exist");
            return false;
        }
 
        printSolution(board);
        return true;
    }
}
