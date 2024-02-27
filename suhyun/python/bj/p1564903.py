def pro(x):
    if x == m:
        for s in selected:
            sys.stdout.write(str(s) + ' ')
        sys.stdout.write('\n')
    else:
        for cand in range(1, n+1):
            if visited[cand] == 0:
                selected[x] = cand
                visited[cand] = 1
                pro(x + 1)
                visited[cand] = 0

import sys
n, m = tuple(map(int, input().split()))
selected = [0 for _ in range(m)]
visited = [0 for _ in range(0, n+1)]
pro(0)