arr = []

for i in range(9):
    a = int(input())
    arr.append(a)

b = max(arr)
print(b)
print(arr.index(b) + 1)    