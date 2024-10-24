
def fib(n):
    if n == 0 or n == 1:
        return n
    a = fib(n-1)
    b = fib(n-2)
    
    return a + b


x = fib(5)