import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split())) # 2, 3, 1
B = [(x, i) for i, x in enumerate(a)] # (2, 0), (3, 1), (1, 2)
B.sort() # (1, 2) (2, 0), (3, 1)
# print(B)
P = [0 for _ in range(n)]
for i in range(n):
    P[B[i][1]] = i
for i in range(n):
    print(P[i], end=' ')