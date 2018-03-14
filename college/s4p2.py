# WAP to print Fibonacci series of n numbers, where n is given by the programmer.


def fib(num):
    a, b = 1, 1
    for i in range(num):
        print(a, end=' ')
        a, b = b, a + b


n = int(input("N: "))
fib(n)
