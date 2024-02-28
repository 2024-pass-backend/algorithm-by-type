def pro(arr):
    for i in range(9):
        # 가로, 세로
        ga = [0] * 10
        se = [0] * 10
        for j in range(9):
            ga[arr[i][j]] += 1
            if ga[arr[i][j]] > 1:
                return 0
            se[arr[j][i]] += 1
            if se[arr[j][i]] > 1:
                return 0
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            list33 = [0] * 10
            for row in range(i, i + 3):
                for col in range(j, j+3):
                    list33[arr[row][col]] += 1
                    if list33[arr[row][col]] > 1:
                        return 0
    return 1
            
t = int(input())
for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = pro(arr)
    print(f'#{tc} {result}')
    