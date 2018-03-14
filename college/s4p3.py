# WAP read a set of numbers from keyboard & to find the sum of all elements of the given array using function.


def sum(numbers):
    sum = 0
    for nums in numbers:
        sum += nums
    return sum

in_numbers = [float(x) for x in input("numbers split by space\n-> ").split()]
print(sum(in_numbers))
