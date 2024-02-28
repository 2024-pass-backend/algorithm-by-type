import sys
n, m = map(int, sys.stdin.readline().split(' '))
selected = [0] * m
visited = [0] * (n + 1)
nums = [i for i in range(1, n+1)] # [1, 2, 3, 4]

def pro(idx):
    if idx == m:
        for elem in selected:
            print(elem, end=' ')
        print()
    
    else:
        for cand in range(1, n+1):
            if visited[cand] == 0:
                selected[idx] = cand
                visited[cand] = 1
                pro(idx + 1)
                visited[cand] = 0
    
pro(0)
    