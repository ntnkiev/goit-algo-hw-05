def caching_fibonacci() -> int:
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        else: 
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci

fib = caching_fibonacci()

def main():
    print(fib(10))

if __name__ == "__main__":
    main()