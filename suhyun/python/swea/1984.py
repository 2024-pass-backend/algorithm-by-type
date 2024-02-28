t = int(input())
for i in range(1, t+1):
    a = list(map(int, input().split()))
    min_val = min(a)
    max_val = max(a)
    sum = 0
    for j in a:
        if j == min_val or j == max_val:
            continue
        sum += j
    print(f'#{i} {round(sum / 8)}')