#include<stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//TODO: Struct mit Int* und Size entwerfen!!!

int* append(int arr[], int n, int elem){
    const int size = n+1; // increasing the size
    int* arrnew = malloc(size*sizeof(int)); // Creating the new array:

    for(int i = 0; i<size;i++){
        arrnew[i] = arr[i]; // copy the element old array to new array:
    }
    arrnew[n] = elem; // Appending the element

    return arrnew;
}


int* removeDupl(int* n, int length){
    int* sol = malloc(1*sizeof(int));
    int sol_length = 1;
    //printf("%d ", length);
    for(int i = 0; i<length; i++){
        bool dupl = false;
        //printf("%d ", sol_length);
        for(int j=0; j<sol_length; j++){
            //printf("%d ", n[i]);
            //printf("%d ", sol[j]);
            if (n[i] == sol[j]){
                dupl = true;
                continue;
            }
        
        }
        if(dupl == false){
            sol = append(sol, sol_length, n[i]);
            sol_length++;
        }        
    }
    return sol;
}

int main(int argc, char *argv[]) {
    int n[4] = {1,2,2,3};
    int* sol = removeDupl(n, sizeof(n)/sizeof(int));
    for (int i=0; i<5; i++){
        printf("%d ", sol[i]);
    }
    return 0;
}