import sys
si = sys.stdin.readline
n = int(si())
a = list(map(int, si().split()))
m = int(si())
a.sort()
ans = []

def binary_search(a, l, r, x):
    answer = 0
    while(l <= r):
        mid = (l + r) // 2
        if a[mid] == x:
            answer += 1
        
        if a[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return answer

for x in map(int, si().split()):
    ans.append(binary_search(a, 0, len(a) - 1, x))

print(*ans)
        