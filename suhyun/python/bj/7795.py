import sys
si = sys.stdin.readline
t = int(si())

# 3 6

# 1

def binary_search(b, l, r, x):
    ans = l - 1
    while(l <= r):
        mid = (l + r) // 2
        if b[mid] >= x:
            r = mid - 1
        else:
            l = mid + 1
            ans = mid
    return ans       


for tc in range(t):
    n, m = map(int, si().split())
    a = list(map(int, si().split()))
    b = list(map(int, si().split()))
    b.sort()
    answer = 0
    # aa = dict()
    for x in a:
        answer += (binary_search(b, 0, len(b) - 1, x) + 1)
        # aa[x] = answer
    
    # print("answer = " + str(answer))
    print(answer)