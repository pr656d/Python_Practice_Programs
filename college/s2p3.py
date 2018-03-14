# WAP to find average of n numbers using while loop

n = int(input("How much numbers? : "))
result = 0
i = 0

if n < 0:
    print("Enter positive number.")
else:
    while i <= n:
        result += i
        i += 1
    print("Average:", result/n)
