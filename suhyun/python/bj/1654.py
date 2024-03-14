## 파이썬에서 int의 범위인 21억은 1 << 31로 표현한다.
import sys
si = sys.stdin.readline
k, n = map(int, si().split())
a = [int(si()) for _ in range(k)]

# print(a)

def determination(H):
    sum = 0
    for x in a:
        if x >= H:
            sum += (x // H)
    return sum >= n
            
            
ans, l, r = 0, 0, 1 << 31
while(l <= r):
    mid = (l + r) // 2
    if determination(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)