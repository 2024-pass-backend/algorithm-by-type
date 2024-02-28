t = int(input())
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    num = 1
    x, y = 0, -1
    d = 0
    while num <= (n * n):
        nx, ny = x + dir[d][0], y + dir[d][1]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            arr[nx][ny] = num
            num += 1
            x, y = nx, ny
        else:
            d = (d + 1) % 4
    print(f'#{tc}')
    for row in arr:
        print(*row)