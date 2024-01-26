import sys
import numpy as np

def read_energy(file):
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
    
    return energy

def read_time(file):
    f = open(file, "r")
    lines = f.readlines()
    time = []
    for line in lines:
        if "Duration" in line:
            time.append(float(line.split(" ")[-2]))

    return time

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
        energy_c = read_energy(file_c)
        energy_java = read_energy(file_java)
        energy_py = read_energy(file_py)
        time_c = read_time(file_c)
        time_java = read_time(file_java)
        time_py = read_time(file_py)

        print(test_dict[entry])
        print(test_dict[entry] + " Energy in C Median: " + str(np.median(energy_c)) + " uJ Average: " + str(np.mean(energy_c)) + " uJ")
        print(test_dict[entry] + " Time in C Median: " + str(np.median(time_c)) + " us Average: " + str(np.mean(time_c)) + " us")
        print()
        print(test_dict[entry] + " Energy in Java: " + str(np.median(energy_java))+ " uJ Average: " + str(np.mean(energy_java))+ " uJ")
        print(test_dict[entry] + " Time in Java: " + str(np.median(time_java))+ " us Average: " + str(np.mean(time_java))+ " us")
        print()
        print(test_dict[entry] + " Energy in Python: " + str(np.median(energy_py)) + "uJ Average: " + str(np.mean(energy_py))+ " uJ")
        print(test_dict[entry] + " Time in Python: " + str(np.median(time_py))+ " us Average: " + str(np.mean(time_py))+ " us")
        print()
        print()



    return 0



if __name__ == "__main__":
    main()