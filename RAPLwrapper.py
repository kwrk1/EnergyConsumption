import os
import subprocess
from typing import List

import pyRAPL

pyRAPL.setup()


@pyRAPL.measureit
def run_py(folder, name):
    path = folder + "/" + name + ".py"
    subprocess.run(["/bin/python3", path], stdout=open(os.devnull, 'wb'))
    return 0

def compile_run_java(folder, name):
    path = folder + "/" + name + ".java"
    out_dir = folder + "/"
    subprocess.run(["/bin/javac", path, "-d", out_dir])
    run_java(folder, name)

@pyRAPL.measureit
def run_java(folder, name):
    path = folder + "/" 
    subprocess.run(["/bin/java", "-cp", path, name], stdout=open(os.devnull, 'wb'))

def compile_run_c(folder, name):
    path = folder + "/" + name + ".c"
    out_dir = folder + "/" + name
    subprocess.run(["/bin/gcc", path, "-o", out_dir])
    run_c(folder, name)


#silent funkt hier nicht
@pyRAPL.measureit
def run_c(folder, name):
    path = folder + "/" + name
    subprocess.run(path, stdout=open(os.devnull, 'wb'))


#energy cost varieren häufig vllt 100 mal messen?
#folder, names für alle in dict speichern
def main():
    folder = "graph_random_const"
    name = "graphconstuction"
    compile_run_c(folder, name)
    compile_run_java(folder, name)
    run_py(folder, name)

if __name__ == "__main__":
    main()