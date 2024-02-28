def rotate_90(arr):
    n = len(arr)
    new_arr = [[0] * n for i in range(n)]
    for row in range(0, n):
        for col in range(0, n):
            new_arr[row][col] = arr[n - col - 1][row]
    return new_arr
            

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    list90 = rotate_90(arr)
    list180 = rotate_90(list90)
    list270 = rotate_90(list180)
    print(f'#{tc}')
    
    for i in range(n):
        for j in range(n):
            print(list90[i][j], end='')
        
        print('', end=' ')

        for k in range(n):
            print(list180[i][k], end='')
        
        print('', end=' ')
        
        for r in range(n):
            print(list270[i][r], end='')
        
        print()
            
    
    