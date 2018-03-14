# WAP to demonstrate tuple operations


tup = ('1', '2', '3', 'Hello')
print("Tup:", tup)
new = input("Enter something to add in tuple: ")
tup += (new,)
print("Tup:", tup)
print(input("Enter something to find in tuple: ") in tup)
print("Slicing tup[1:3]:", tup[1:3])
print("Deleting tup...")
del tup
print("Tup deleted.")