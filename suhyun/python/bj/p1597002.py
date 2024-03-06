# 5
# 0 1
# 1 2
# 3 1
# 4 2
# 5 1 

# 흰색 - [0, 3, 5]
# 검은색 - [1, 4]

import sys
n = int(sys.stdin.readline())

a = [[] for _ in range(n+1)] # 6개의 빈 배열 생성

for i in range(n):
    coord, color = map(int, sys.stdin.readline().split())
    a[color].append(coord)
    
def toLeft(color, i):
    if i == 0:
        return 100000
    return a[color][i] - a[color][i - 1]

def toRight(color, i):
    if i + 1 == len(a[color]):
        return 100000
    return a[color][i + 1] - a[color][i]
    
ans = 0
for color in range(1, n+1):
    a[color].sort()
    for i in range(len(a[color])):
        ans += min(toLeft(color, i), toRight(color, i))

print(ans)