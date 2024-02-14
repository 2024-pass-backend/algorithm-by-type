t = int(input())

for i in range(1, t+1):
    n = int(input())
    arr = [[0] * n for i in range(n)]
    for j in range(n):
        arr[j][0] = 1
    
    for j in range(1, n):
        for k in range(1, n):
            arr[j][k] = arr[j-1][k-1] + arr[j-1][k]
    
    print(f'#{i}')
    for j in range(n):
        for k in range(n):
            if arr[j][k] == 0:
                continue
            print(arr[j][k], end=' ')
        print()