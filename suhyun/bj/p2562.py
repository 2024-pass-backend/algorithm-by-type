arr = []
max_val = 0

for _ in range(9):
    a = int(input())
    arr.append(a)
    if a > max_val:
        max_val = a

arr.sort()
##print(arr)
##print(max_val)

i = arr.index(max_val)

print(max_val)
print(i+1)