# WAP that demonstrates the use break and continue statements to alter the flow of the loop.


while True:
    name = str(input("Name: "))
    if name.isalpha():
        print("Hello %s" % name)
        break
    else:
        print("Invalid name.\n")
        continue
