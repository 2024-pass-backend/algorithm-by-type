t = int(input())
for tc in range(1, t+1):
    n, k = tuple(map(int, input().split()))
    arr = [list(map(int, input().split())) for i in range(n)]
    cnt = 0

    for i in range(n):
        sum = 0
        
        for j in range(n):
            if arr[i][j] == 1:
                sum += 1
            if arr[i][j] == 0 or j == n-1:
                if sum == k:
                    cnt += 1
                sum = 0
        
        for j in range(n):
            if arr[j][i] == 1:
                sum += 1
            if arr[j][i] == 0 or j == n-1:
                if sum == k:
                    cnt += 1
                sum = 0
    
    print(f'#{tc} {cnt}')
            
                
        