n = int(input())
array = [[0] * 100 for _ in range(100)] ## 100 * 100 배열
for _ in range(n):
    y1, x1 = map(int, input().split()) #3,7
    
    for i in range(x1, x1+10): #7부터 17
        for j in range(y1, y1+10): #3부터 13
            array[i][j] = 1

result = 0
for k in range(100):
    result += array[k].count(1)
        