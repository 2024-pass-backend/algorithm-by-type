import sys
si = sys.stdin.readline
t = int(si())

# 1 3 6

def binary_search(b, l, r, x):
    ans = -1
    while(l <= r):
        mid = (l + r) // 2
        if b[mid] < x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans
            

for tc in range(t):
    a, b = map(int, si().split())
    a_arr = list(map(int, si().split()))
    b_arr = list(map(int, si().split()))
    b_arr.sort() # 1 3 6
    answer = 0
    for elem in a_arr:
        answer += (binary_search(b_arr, 0, len(b_arr) - 1, elem) + 1)
    print(answer)
    