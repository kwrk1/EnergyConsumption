public class fib {

    public int fibonacci(int n) {
        if(n<=1){
            return n;
        }
        return fibonacci(n-1) + fibonacci(n-2);        
    }
	public static void main(String[] args){
        
        fib fib = new fib();
		System.out.println(fib.fibonacci(35));	
	}
}