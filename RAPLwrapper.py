import os
import shutil
import subprocess
import sys
from os import path
from pathlib import Path
from typing import List

import pyRAPL

pyRAPL.setup()

@pyRAPL.measureit
def run_py(folder, name):
    path = folder + "/" + name + ".py"
    subprocess.run(["/bin/python3", path], stdout=open(os.devnull, 'wb'))
    return 0

#silent funkt hier nicht
@pyRAPL.measureit
def run_c(folder, name):
    path = folder + "/" + name
    subprocess.run(path, stdout=open(os.devnull, 'wb'))

@pyRAPL.measureit
def run_java(folder, name):
    path = folder + "/" 
    subprocess.run(["/bin/java", "-cp", path, name], stdout=open(os.devnull, 'wb'))

def compile_c(folder, name):
    if name == "dijkstra":
        path1 = folder + "/" + name + ".c"
        path2 = folder + "/" + "graphconstruction.c"
        out_dir = folder + "/" + name
        subprocess.run(["/bin/gcc", path1, path2, "-o", out_dir])
    else:
        path = folder + "/" + name + ".c"
        out_dir = folder + "/" + name
        subprocess.run(["/bin/gcc", path, "-o", out_dir])

def compile_java(folder, name):
    path = folder + "/" + name + ".java"
    out_dir = folder + "/"
    subprocess.run(["/bin/javac", path, "-d", out_dir])
    

def compile_everything(dict):
    for entry in dict:
        compile_c(entry, dict[entry])
        compile_java(entry, dict[entry])

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
    
    for entry in test_dict:
        
        file = test_dict[entry] + "_c.txt"
        f = open(file, "w")
        sys.stdout = f
        for i in range(0, 101):
            run_c(entry, test_dict[entry])

        file = test_dict[entry] + "_java.txt"
        f = open(file, "w")
        sys.stdout = f
        for i in range(0, 101):
            run_java(entry, test_dict[entry])

        file = test_dict[entry] + "_py.txt"
        f = open(file, "w")
        sys.stdout = f
        for i in range(0, 101):
            run_py(entry, test_dict[entry])


if __name__ == "__main__":
    main()