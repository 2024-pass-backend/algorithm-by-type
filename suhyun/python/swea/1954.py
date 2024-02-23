t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * n for i in range(n)]
    cnt = 1
    for i in range(n):
        for j in range(n):
            arr[i][j] = cnt
            cnt += 1