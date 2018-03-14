# WAP to print Fibonacci series of numbers, where n is given by the programmer


def fib(n):
    a, b = 1, 1
    for i in range(n):
        print(a)
        a, b = b, a + b


fib(5)
