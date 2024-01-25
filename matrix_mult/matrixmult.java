package matrix_mult;

public class matrixmult {


    public static int[][] matrix_mult(int[][] m_one, int[][] m_two) {
        int m_one_rows = m_one.length;
        int m_one_cols = m_one[0].length;
        int m_two_rows = m_two.length;
        int m_two_cols = m_two[0].length;
        
        // change this
        if (m_one_cols == m_two_rows) {

            // init result matrix
            int[][] result_matrix = new int[m_one_rows][m_two_cols];

            for (int i = 0; i < m_one_rows; i++) {
                for (int j = 0; j < m_two_cols; j++) {
                    int cell = 0;
                    
                    for (int k = 0; k < m_one_cols; k++) {
                        cell = cell + (m_one[i][k] * m_two[k][j]);
                    }

                    result_matrix[i][j] = cell;
                }
            }
            return result_matrix;
        } else {
            int[][] result_matrix = new int[m_one_rows][m_two_cols];
            System.out.println("dis shit illegal");
            return result_matrix;
        }
        
    }


    public static void main(String[] args){
        
        int[][] m_one = {
            {2, 3, 4, 5, 6},
            {2, 3, 4, 5, 6},
            {2, 3, 4, 5, 6},
        };

        int[][] m_two = {
            {2, 3, 4},
            {2, 3, 4},
            {2, 3, 4},
            {2, 3, 4},
            {2, 3, 4},
        };

        int result_matrix[][] = matrix_mult(m_one, m_two);

        for (int i = 0; i < result_matrix.length; i++) {
            for (int j = 0; j < result_matrix[0].length; j++) {
                System.out.println(result_matrix[i][j]);
            }
        }
    }
}