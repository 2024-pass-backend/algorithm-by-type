arr = [[0] * 100 for i in range(100)]
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for row in range(y, y+10):
        for col in range(x, x+10):
            arr[row][col] = 1

cnt = 0
for i in arr:
    for j in i:
        if j == 1:
            cnt += 1
            
print(cnt)     