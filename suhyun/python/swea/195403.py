t = int(input())
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    start = 1
    x, y = 0, -1
    direction = 0

    while(start <= n * n):
        nx = x + dir[direction][0]
        ny = y + dir[direction][1] 
        if nx < 0 or ny < 0 or nx >= n or ny >= n or arr[nx][ny] != 0:
            direction = (direction + 1) % 4
        else:
            arr[nx][ny] = start
            start += 1
            x, y = nx, ny
    print(f'#{tc}')
    for row in arr:
        print(*row)
                
            
                
            
        
        