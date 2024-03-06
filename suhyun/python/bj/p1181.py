n = int(input())
arr = [input() for _ in range(n)]
arr.sort(key = lambda x: (len(x), x))

print(arr[0])
for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        continue
    print(arr[i])