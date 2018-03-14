# multiply using recursions


def multi(num, base):
    if base == 1:
        return num
    else:
        return num + multi(a, base - 1)


a = int(input("Number: "))
b = int(input("Times to multiply: "))
print(a, "*", b, "=", multi(a, b))
