t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        # 가로
        cnt_ga = 0
        for j in range(n):
            if arr[i][j] == 1:
                cnt_ga += 1
            if arr[i][j] == 0 or j == n-1:
                if cnt_ga == m:
                    ans += 1
                cnt_ga = 0
        
        cnt_se = 0
        for j in range(n):
            if arr[j][i] == 1:
                cnt_se += 1
            if arr[j][i] == 0 or j == n-1:
                if cnt_se == m:
                    ans += 1
                cnt_se = 0
            
    print(f'#{tc} {ans}')