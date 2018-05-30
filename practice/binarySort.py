l = [5, 11, 6, 1, 2, 9, 0]
l.sort()
beg = 0
end = len(l)
key = int(input())
print(l)

while True:
    if beg >= end:
        print("Key not found!")
        break

    mid = (beg + end) // 2

    if l[mid] == key:
        print("Key found at %d" % mid)
        break
    elif l[mid] > key:
        end = mid - 1
        continue
    elif l[mid] < key:
        beg = mid + 1
        continue
    else:
        print("Something went wrong!")
        break
