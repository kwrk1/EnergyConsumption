import sys
import numpy as np

def read_file(file):
    f = open(file, "r")
    lines = f.readlines()
    found = False
    energy = []
    for line in lines:
        if "PKG" in line:
            found = True
            continue

        if found == True:
            energy.append(float(line.split(" ")[-2]))
            found = False
    
    return np.median(energy)


def main():
    test_dict = {
        'SieveOfErathosthenes'  : 'sieve',
        'RemoveDuplicates'      : 'removedupl',
        'Quicksort'             : 'qsort',
        'NQueens'               : 'nqueens',
        'MatrixMult'            : 'matrixmult',
        'graph_random_const'    : 'graphconstruction',
        'graph_dijkstra'        : 'dijkstra',
        'Fibonacci'             : 'fib',
    }


    #dataframe??? als output mit unterschiedlichen n, median, average
    f = open("results.txt", "w")
    sys.stdout = f
    for entry in test_dict:
        file_c = "results/" + test_dict[entry] + "/" + test_dict[entry] + "_c.txt"
        file_java = "results/" + test_dict[entry] + "/" + test_dict[entry] + "_java.txt"
        file_py = "results/" + test_dict[entry] + "/" + test_dict[entry] + "_py.txt"
        print("Median of " + test_dict[entry] + " in C: " + str(read_file(file_c)))
        print("Median of " + test_dict[entry] + " in Java: " + str(read_file(file_java)))
        print("Median of " + test_dict[entry] + " in Python: " + str(read_file(file_py)))
        


    return 0



if __name__ == "__main__":
    main()