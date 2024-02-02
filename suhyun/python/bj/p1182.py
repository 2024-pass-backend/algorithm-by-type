import sys
n, m = tuple(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
ans = 0

def rec_func(k, sum):
    if k == n:
        global ans
        if sum == m:
            ans += 1
    else:
        rec_func(k + 1, sum)
        rec_func(k + 1, sum + arr[k])


rec_func(0, 0)
if m == 0:
    ans -= 1
print(ans)