import sys
n = int(sys.stdin.readline().rstrip())
row = [-1] * n
result = 0

def dfs(x):
    global result
    if x == n:
        result += 1
        return
    for i in range(n):
        if okay(x, i):
            row[x] = i
            dfs(x + 1)
            row[x] = -1

def okay(x, y):
    for i in range(x):
        if row[i] == y or abs(row[i] - y) == x - i:
            return False
    return True

dfs(0)
print(result)
