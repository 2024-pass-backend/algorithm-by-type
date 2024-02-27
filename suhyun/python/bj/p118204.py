def pro(idx, sum):
    if idx == n:
        global cnt
        if sum == s:
            cnt += 1
    else:
        pro(idx + 1, sum)
        pro(idx + 1, sum + arr[idx]) 
        
import sys
n, s = tuple(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
pro(0, 0)

if s == 0:
    cnt -= 1
print(cnt)