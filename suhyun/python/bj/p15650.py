def pro(x):
    if x == m:
        for s in selected:
            sys.stdout.write(str(s) + ' ')
        sys.stdout.write('\n')
    else:
        if x == 0:
            start = 1
        else:
            start = selected[x - 1] + 1

        for cand in range(start, n+1):
            selected[x] = cand
            pro(x + 1)

import sys
n, m = tuple(map(int, sys.stdin.readline().split()))
selected = [0 for _ in range(m)]
pro(0)