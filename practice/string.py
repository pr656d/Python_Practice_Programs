str = 'HELLO'
n = -len(str)

for i in str:
    print(i, end='')

print()

for n in str[::-1]:
    print(n, end='')
