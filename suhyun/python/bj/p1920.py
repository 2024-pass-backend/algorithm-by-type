import sys
si = sys.stdin.readline
n = int(si())
a = list(map(int, si().split()))
a.sort()

def bin_search(a, l, r, x):
    while l <= r:
        mid = (l + r) // 2 # 2
        if a[mid] == x:
            return True
        if a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return False



m = int(si())
for x in map(int, si().split()):
    if bin_search(a, 0, n-1, x):
        print(1)
    else:
        print(0)

# 5
# 4 1 5 2 3 >> 1 2 3 4 5
# 5
# 1 3 7 9 5