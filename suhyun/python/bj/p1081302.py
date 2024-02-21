n, m = tuple(map(int, input().split()))

arr = [i for i in range(n+1)]
    
for i in range(m):
    a, b = tuple(map(int, input().split()))
    arr[a], arr[b] = arr[b], arr[a]

for x in range(1, len(arr)):
    print(arr[x], end=' ')