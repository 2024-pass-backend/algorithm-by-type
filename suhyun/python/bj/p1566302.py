import sys
n, m = map(int, sys.stdin.readline().split(' '))
nums = sorted(list(map(int, sys.stdin.readline().split(' '))))
selected = [0] * m
used = [0] * n

def pro(k):
    if k == m:
        for x in selected:
            sys.stdout.write(str(x) + ' ')
        sys.stdout.write('\n')
    
    else:
        last_cand = 0
        for cand in range(0, n):
            if used[cand] == 1 or last_cand == nums[cand]:
                continue
            
            last_cand = nums[cand]
            selected[k] = nums[cand]
            used[cand] = 1
            pro(k + 1) 
            used[cand] = 0

pro(0)