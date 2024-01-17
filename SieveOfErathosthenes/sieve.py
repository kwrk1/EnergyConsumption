from typing import List

def SieveOfErathosthenes(n: int):
    primes = [True] * (n+1)
    p = 2
    while (p*p <= n):
        if primes[p] == True:
            i = p*p
            while(i<=n):
                primes[i]= False
                i += p
        p += 1
        
    for p in range(2, n+1):
        if primes[p]:
            print(p)

def main():
    SieveOfErathosthenes(10)

if __name__ == "__main__":
    main()