# pattern printing

n = int(input("n: "))

for i in range(n):
    for j in range(i+1):
        if i >= j:
            print(j, end = '')
        else:
            print(" ", end = '')
    print()
