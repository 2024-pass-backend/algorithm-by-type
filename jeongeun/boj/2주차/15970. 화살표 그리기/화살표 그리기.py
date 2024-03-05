import sys

group = {}

for _ in range(int(input())):
    x,y=map(int, sys.stdin.readline().rstrip().split())
    if y not in group:
        group[y] = []
    group[y].append(x)

for c in group:
        group[c].sort()
        
ans=0

for c, g in group.items():
    for i in range(len(g)):
        if i == 0:
            d = g[i + 1] - g[i]
        elif i == len(g) - 1:
            d = g[i] - g[i - 1]
        else:
            d = min(g[i] - g[i - 1], g[i + 1] - g[i])
        ans += d
print(ans)