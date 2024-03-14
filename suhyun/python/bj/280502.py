import sys
si = sys.stdin.readline
n, m = map(int, si().split())
a = list(map(int, si().split()))

def determination(H):
    sum = 0
    for x in a:
        if x > H:
            sum += (x - H)
    return sum >= m

ans, l, r = 0, 0, 2000000000

while(l <= r):
    mid = (l + r) // 2
    if determination(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)