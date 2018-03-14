# WAP to find N! using function


def fact(num):
    s = 1
    for i in range(1, num+1):
        s *= i
    return s


numIn = int(input("num: "))
if numIn < 0:
    print("Not exist.")
else:
    print("factorial of", numIn, ":", fact(numIn))
