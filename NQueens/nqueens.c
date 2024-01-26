#include <stdbool.h>
#include <stdio.h>

#define N 4

void printSolution(int board[N][N]){
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if(board[i][j])
                printf("Q ");
            else
                printf(". ");
        }
        printf("\n");
    }
}

bool isSafe(int board[N][N], int row, int col){ 
    for (int i = 0; i < col; i++)
        if (board[row][i])
            return false;

    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return false;

    for (int i = row, j = col; j >= 0 && i < N; i++, j--)
        if (board[i][j])
            return false;
 
    return true;
}
 

bool solveNQ(int board[N][N], int col){

    if (col >= N){
        return true;
    }
        
    for (int i = 0; i < N; i++) {
         
        if (isSafe(board, i, col)) {

            board[i][col] = 1;
 
            if (solveNQ(board, col + 1))
                return true;

            board[i][col] = 0;
        }
    }
 
    return false;
}



int main(int argc, char *argv[]) {
    int board[N][N] = { { 0, 0, 0, 0 },
                        { 0, 0, 0, 0 },
                        { 0, 0, 0, 0 },
                        { 0, 0, 0, 0 } };
 
    if (solveNQ(board, 0) == false) {
        printf("Solution does not exist");
    } else {
        printSolution(board);
    }   

    return 0;
}