arr = []
for _ in range(9):
    x = int(input())
    arr.append(x)

y = max(arr)

print(y)
print(arr.index(y) + 1)