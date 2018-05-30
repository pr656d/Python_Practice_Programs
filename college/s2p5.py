# WAP to print multiplication table

num = int(input("Number: "))
for i in range(1, 11):
    print("%2d * %2d = %d" % (num, i, num * i))
