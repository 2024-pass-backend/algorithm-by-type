t = int(input())
for tc in range(1, t+1):
    n = int(input())
    dist = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    arr = [[0] * n for _ in range(n)]
    num = 1 # 달팽이를 채울 숫자
    d = 0 # 달팽이 이동방향
    x, y = 0, -1
    while num <= (n*n):
        nx, ny = x + dist[d][0], y + dist[d][1]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            arr[nx][ny] = num
            num += 1
            x, y = nx, ny
        else:
            d = (d + 1) % 4
    print(f'#{tc}')
    for row in arr:
        print(*row)