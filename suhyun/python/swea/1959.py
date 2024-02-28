t = int(input())
for tc in range(1, t+1):
    n, m = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_val = 0
    
    if n > m:
        for i in range(n - m + 1):
            sum = 0
            idx = 0
            for j in range(i, i+m):
                sum += a[j] * b[idx]
                idx += 1
            max_val = max(max_val, sum)
    elif n < m:
        for i in range(m - n + 1):
            sum = 0
            idx = 0
            for j in range(i, i+n):
                sum += a[idx] * b[j]
                idx += 1
            max_val = max(max_val, sum)               
    else:
        sum = 0
        for i in range(n):
            sum += a[i] * b[i]
        max_val = max(max_val, sum)
    
    print(f'#{tc} {max_val}')