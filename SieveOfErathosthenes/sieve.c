#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



void SieveOfErathosthenes(int n){
    bool primes[11]; //n+1 funktioniert nicht obwohl es seit C99 funktionieren sollte

    memset(primes, true, sizeof(primes));
    int p = 2;
    while(p*p <= n) {
        
        if (primes[p] == true) {
            int i = p * p;
            while (i <= n){
                primes[i] = false;
                i += p;
            }
        p++;
        }
    }
 
    for (int p = 2; p <= n; p++)
        if (primes[p] == true)
            printf("%d ",p);

}

int main(int argc, char *argv[]) {
    SieveOfErathosthenes(10);

    return 0;
}