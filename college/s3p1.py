# WAP which will print a string as it is except # and done is entered.
# If # is entered ask the user to enter the new string and
# done is entered terminate the program.

while True:
    line = str(input("> "))
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)