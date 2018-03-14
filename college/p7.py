# WAP to read a set of numbers in an array & to find the largest of them


def largest(arr):
    return max(arr)


arr = list()
num = input("How many elements you want to store? ")

for i in range(int(num)):
    num = input("Num: ")
    arr.append(int(num))

print(largest(arr))
