# WAP to create a function to swap values of a pair of integers


def swap(a, b):
    a, b = b, a
    return (a, b)


in_a, in_b = input("a: "), input("b: ")
print("Before swap a:", in_a, " b:", in_b)
s = swap(in_a, in_b)
print("After swap a:", s[0], " b:", s[0])
