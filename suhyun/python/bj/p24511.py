import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # 4
a = list(map(int, input().split())) # 0 1 1 0
b = list(map(int, input().split())) # 1 2 3 4
m = int(input()) # 3
c = list(map(int, input().split())) # 2 4 7

queue = deque([])
for i in range(n):
    if a[i] == 0:
        queue.appendleft(b[i])
    else:
        if queue == []:
            print(*c)
            sys.exit()

for i in range(m):
    queue.append(c[i])
    print(queue.popleft(), end = " ")