def fib(n: int) -> int:
    if (n<=1):
        return n
    
    return fib(n-1) + fib(n-2)


def main():
    print(fib(35))

if __name__ == "__main__":
    main()