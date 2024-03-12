import sys
si = sys.stdin.readline

n = int(si())
a = list(map(int, si().split()))
b = int(si())

a.sort()
answer = 0

def binary_search(a, l, r, x):
    while(l <= r):
        mid = (l + r) // 2
        if a[mid] == x:
            return True
        
        if a[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return False

for x in a:
    if binary_search(a, 0, len(a) - 1, b - x):
        answer += 1

print(answer // 2)