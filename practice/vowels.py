s = str(input("Enter String: "))
count = 0
for i in range(len(s)):
    if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
        count += 1

print(s)
print('Numbers of vowels: ', str(count))
