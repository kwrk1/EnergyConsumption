#include<stdio.h>
#include<limits.h>
#include<stdlib.h>

// structs
typedef struct MatrixCol
{
    unsigned int* matrix_col;
    unsigned int cap;
} MatrixCol;

typedef struct IntMatrix
{
    MatrixCol** matrix_row;
    unsigned int cap;
} IntMatrix;


// global vars
// from legacy code
short int ERROR_CODE = 0;


// methods
int int_alloc_onedim(MatrixCol *self, unsigned int size)
{
    self->cap = 0;
    self->matrix_col = malloc(size * sizeof(unsigned int));

    if(self->matrix_col == NULL)
    {
        fprintf(stderr, "*3* ERROR : FAILED TO ALLOCATE MEMORY FOR IntList!\n");
        ERROR_CODE = 3;
        return ERROR_CODE;
    }
    
    for(int i = 0; i < size; i++) {
        self->matrix_col[i] = 0;
    }

    self->cap = size;

    return 0;
}


int int_alloc_twodim(IntMatrix *self, unsigned int row_size, unsigned int col_size)
{
    self->cap = 0;
    self->matrix_row = (MatrixCol**) malloc(row_size * sizeof(MatrixCol));

    if(self->matrix_row == NULL)
    {
        fprintf(stderr, "*3* ERROR : FAILED TO ALLOCATE MEMORY FOR IntMatrix!");
        ERROR_CODE = 3;
        return ERROR_CODE;
    }
    
    self->cap = row_size;

    for (int i = 0; i < self->cap; i++) {
        self->matrix_row[i] = (MatrixCol*) malloc(sizeof(MatrixCol));
        if(self->matrix_row[i] == NULL || int_alloc_onedim(self->matrix_row[i], col_size) != 0)
        {
            if(self->matrix_row[i] == NULL)
            {
                fprintf(stderr, "*3* ERROR : FAILED TO ALLOCATE MEMORY FOR matrix_row[%d]!", i);
                ERROR_CODE = 3;
                return ERROR_CODE;
            }
            fprintf(stderr, "*3* ERROR : FAILED TO ALLOCATE MEMORY FOR IntList IN matrix_row[%d]!", i);
            return ERROR_CODE;
        }
    }

    return 0;
}

int randInRange(int min, int max)
{
  return min + (int) (rand() / (double) (RAND_MAX) * (max - min + 1));
}

IntMatrix* matrix_mult(IntMatrix *m_one, IntMatrix *m_two) {
    int m_one_rows = m_one->cap;
    int m_one_cols = m_one->matrix_row[0]->cap;
    int m_two_rows = m_two->cap;
    int m_two_cols = m_two->matrix_row[0]->cap;

    if (m_one_cols == m_two_rows) {

        IntMatrix *result_matrix = (IntMatrix*) malloc(sizeof(IntMatrix));
        int_alloc_twodim(result_matrix, m_one_rows, m_two_cols);

        for (int i = 0; i < m_one_rows; i++) {
            for (int j = 0; j < m_two_cols; j++) {
                int cell = 0;

                for (int k = 0; k < m_one_cols; k++) {
                    cell = cell + (m_one->matrix_row[i]->matrix_col[k] * m_two->matrix_row[k]->matrix_col[j]);
                }

                result_matrix->matrix_row[i]->matrix_col[j] = cell;
            }
        }
        return result_matrix;
    } else {
        puts("nonononononono");
    }
    
}

// main
IntMatrix* main(int argc, char *argv[]) {

    //init mat
    IntMatrix* mat_one = (IntMatrix*) malloc(sizeof(IntMatrix));
    int_alloc_twodim(mat_one, 700, 500);

    for (int i = 0; i < mat_one->cap; i++) {
        for (int j = 0; j < mat_one->matrix_row[0]->cap; j++) {
            
            mat_one->matrix_row[i]->matrix_col[j] = randInRange(0, 1000);
        }
    }

    //ínit mat
    IntMatrix* mat_two = (IntMatrix*) malloc(sizeof(IntMatrix));
    int_alloc_twodim(mat_two, 500, 600);

    for (int i = 0; i < mat_two->cap; i++) {
        for (int j = 0; j < mat_two->matrix_row[0]->cap; j++) {
            
            mat_two->matrix_row[i]->matrix_col[j] = randInRange(0, 1000);
        }
    }

    // result matrix
    IntMatrix* result_matrix = matrix_mult(mat_one, mat_two);
    // for (int i = 0; i < result_matrix->cap; i++) {
    //     for (int j = 0; j < result_matrix->matrix_row[0]->cap; j++) {
            
    //         printf("%d, ", result_matrix->matrix_row[i]->matrix_col[j]);
    //     }
    //     printf("\n");
    // }
    
    return result_matrix;
}