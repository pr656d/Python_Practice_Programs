# Write a function to swap value of a pair of integers


def swap(num1, num2):
    print("num1:", num1, "num2:", num2)
    num1, num2 = num2, num1
    print("num1:", num1, "num2:", num2)


num1, num2 = int(input("Num1: ")), int(input("Num2: "))
swap(num1, num2)