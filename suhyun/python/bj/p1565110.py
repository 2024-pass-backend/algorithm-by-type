import sys
def pro(x):
    if x == m:
        for s in selected:
            sys.stdout.write(str(s) + ' ')
        sys.stdout.write('\n')
    
    else:
        for cand in range(1, n+1):
            selected[x] = cand
            pro(x + 1)
            

n, m = tuple(map(int, sys.stdin.readline().split()))
selected = [0 for _ in range(m)]
pro(0)