import sys
n, s = tuple(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0

def rec_func(k, sum):
    if k == n:
        global cnt
        if sum == s:
            cnt += 1
    
    else:
        rec_func(k + 1, sum)
        rec_func(k + 1, sum + arr[k])


rec_func(0, 0)

if s == 0:
    cnt -= 1
print(cnt)

