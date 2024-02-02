n = int(input())
arr = [[0] * 100 for _ in range(100)]

for i in range(n):
    x, y = map(int, input().split()) ## 3,7 ~ 13,17
    
    for j in range(y, y+10):
        for i in range(x, x+10):
            arr[j][i] = 1

result = 0
for i in range(100):
    result += arr[i].count(1)
print(result)