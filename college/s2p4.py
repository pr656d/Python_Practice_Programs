# WAP to find whether the given program is prime or not.


val = int(input("Enter a value: "))

if val > 1:
    for i in range(2, val):
        if (val % i) == 0:
            print("It's not prime")
            break
    else:
        print("It's prime")
else:
    print("It's not prime")
