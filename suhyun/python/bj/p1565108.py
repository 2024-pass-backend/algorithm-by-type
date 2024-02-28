def pro(x):
    if m == x:
        for s in selected:
            sys.stdout.write(str(s) + ' ')
        sys.stdout.write('\n')
    
    else:
        for cand in range(1, n+1):
            selected[x] = cand
            pro(x + 1)
    
import sys
n, m = tuple(map(int, input().split()))
selected = [0 for _ in range(m)]
pro(1)
