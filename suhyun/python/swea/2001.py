t = int(input())

for i in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(n)]
    max_val = 0
    
    for j in range(n-m+1):
        for k in range(n-m+1):
            sum_val = 0
            for row in range(j, j+m):
                for col in range(k, k+m):
                    sum_val += arr[row][col]
            if max_val < sum_val:
                max_val = sum_val
    
    print(f'#{i} {max_val}')
    