import sys
n = int(sys.stdin.readline())

a = [[] for _ in range(n + 1)]
ans = 0

for i in range(n):
    coord, color = map(int, sys.stdin.readline().split(' '))
    a[color].append(coord)

def toLeft(x, color):
    if x == 0:
        return 100000
    else: return a[color][x] - a[color][x - 1]

def toRight(x, color):
    if x + 1 == len(a[color]):
        return 100000
    else: return a[color][x + 1] -a[color][x]
     

for i in range(1, n + 1):
    a[i].sort()
    if len(a[i]) >= 1: 
        for j in range(len(a[i])):
            ans += (min(toLeft(j, i), toRight(j, i)))

print(ans)
    
    