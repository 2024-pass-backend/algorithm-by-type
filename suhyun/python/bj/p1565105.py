import sys

n, m = map(int, sys.stdin.readline().split())
selected = [0 for _ in range(m)]

def rec_func(k):
    if k == m:
        for x in selected:
            sys.stdout.write(str(x) + ' ')
        sys.stdout.write('\n')
    
    else:
        for cand in range(1, n+1):
            selected[k] = cand
            rec_func(k+1)

rec_func(0)