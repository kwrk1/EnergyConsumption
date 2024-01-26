public class sieve {

    public static void SieveOfErathosthenes(int n){
        boolean primes[] = new boolean[n + 1];
        for (int i = 0; i <= n; i++)
            primes[i] = true;

        int p = 2;
        while(p*p<=n){
            if (primes[p] == true){
                int i = p*p;
                while (i<=n){
                    primes[i] = false;
                    i += p;
                }
            }
            p++;
        }

        for (int i=2; i<=n; i++){
            if(primes[i] == true){
                System.err.println(i);
            }
        }

    }
    public static void main(String[] args){                                                                                                                                                                                                                                                                                     
        SieveOfErathosthenes(1000000);
    }
}
