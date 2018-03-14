x = int(input('Enter a integer: '))
ans = 0

while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube.')
else:
    if x < 0:
        x = -x
    print('cube root of ' + str(x) + ' is ' + str(ans) + '.')
