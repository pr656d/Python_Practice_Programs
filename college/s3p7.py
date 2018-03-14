# WAP to demonstrate set operations


my_set = {1, 2, 3}   # predefined set
default_set = set()  # empty set

print("my_set:", my_set, "\n" +
      "default_set:", default_set)
print()

ad = int(input("Enter something to add in set: "))
default_set.add(ad)
my_set.add(ad)
print()

print("my_set:", my_set, "\n" +
      "default_set :", default_set)
print()

print("updating 2,3,5,8...")
my_set.update([2, 3, 5, 8])
default_set.update([2, 3, 5, 8])

print("my_set:", my_set, "\n" +
      "default_set :", default_set)
print()

print("--> Enter anything which exist in set.")
delete = int(input("Enter something to delete using discard: "))
my_set.discard(delete)
default_set.discard(delete)
print()
print("--> Enter something which already exist in set.")
delete = int(input("Enter something to delete using remove: "))
my_set.remove(delete)
default_set.remove(delete)
print("my_set:", my_set, "\n" +
      "default_set :", default_set)
