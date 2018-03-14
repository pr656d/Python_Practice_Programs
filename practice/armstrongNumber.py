# if there is 153 then cube of each number and addition is equal to the number

n = int(input("Enter a number:"))
result = 0
if n < 0:
    print("Enter positive number.")
else:
    temp = n
    while temp > 0:
        digit = temp%10
        result += digit**3
        temp //= 10
if result == n:
    print("Is amrstrom.")
else:
    print("Is not amrstrom.")