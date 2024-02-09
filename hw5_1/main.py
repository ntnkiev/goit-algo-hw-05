def caching_fibonacci() -> int:
    cache = {} #створення порожнього словнику кешу

    def fibonacci(n): #обчислення чисел Фібоначчі
        if n in cache:
            return cache[n] #якщо результат є в кешу: повернення результату
        if n <= 1:
            return n
        else: 
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2) #додавання в кеш нового результату
            return cache[n]
    return fibonacci

fib = caching_fibonacci()

def main():
    print(fib(10))

if __name__ == "__main__":
    main()