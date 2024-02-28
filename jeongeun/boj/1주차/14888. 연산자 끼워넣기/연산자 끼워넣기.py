import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
ad, s, m, d = map(int, sys.stdin.readline().split())

mx = -float('inf')
mn = float('inf')

def bt(i, r, ad, s, m, d):
    global mx, mn
    if i == n:
        mx = max(mx, r)
        mn = min(mn, r)
        return

    if ad:
        bt(i+1, r+a[i], ad-1, s, m, d)
    if s:
        bt(i+1, r-a[i], ad, s-1, m, d)
    if m:
        bt(i+1, r*a[i], ad, s, m-1, d)
    if d:
        bt(i+1, -(-r // a[i]) if r < 0 else r // a[i], ad, s, m, d-1)

bt(1, a[0], ad, s, m, d)
print(mx)
print(mn)