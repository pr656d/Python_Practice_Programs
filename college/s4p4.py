# WAP to demonstrate usage of positional, keyword and default parameters.


# >>> Simply adding three numbers a, b, c
def abc(a, b, c=3):
    return a + b + c


print(abc(5, 2, 3))  # a, b and c are positional arguments and c is overwritten with 3
print(abc(2, 4))  # a, b are positional and c is default argument
print(abc(5, b=5))  # a is positional and b is keyword or named argument and also c is default argument
print(abc(a=4, b=3))  # a and b are keyword or named argument and c is also default argument
print(abc(a=3, b=5, c=7))  # three of them are named or keyword arguments
