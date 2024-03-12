import sys
si = sys.stdin.readline
n = int(si())
a = list(map(int, si().split()))
a.sort()

# 1 2 3 4 5 // 1

def binary_search(a, l, r, x):
    while(l <= r):
        mid = (l + r) // 2
        if a[mid] == x:
            return True
        elif a[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return False


m = int(si())
for x in map(int, si().split()):
    if binary_search(a, 0, n-1, x):
        print(1)
    else:
        print(0)