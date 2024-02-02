arr = []
max_val = 0

for _ in range(9):
    a = int(input())
    arr.append(a)

print(max(arr))
print(arr.index(max(arr)) + 1)