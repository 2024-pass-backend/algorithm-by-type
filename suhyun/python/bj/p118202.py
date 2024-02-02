import sys
n, m = tuple(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
ans = 0

def rec_func(idx, sum):
    if idx == n:
        global ans
        if sum == m:
            ans += 1
    else:
        rec_func(idx + 1, sum + arr[idx])
        rec_func(idx + 1, sum)


rec_func(0, 0)
if m == 0:
    ans -= 1
print(ans)