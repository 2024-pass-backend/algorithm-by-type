# 덧셈(0), 뺄셈(1), 곱셈(2), 나눗셈(3)
import sys
n = int(sys.stdin.readline())
nums = [0] * (n + 1)
arr = list(map(int, sys.stdin.readline().split(' '))) ## n개
for i in range(1, n+1):
    nums[i] = arr[i-1]
operator = list(map(int, sys.stdin.readline().split(' ')))
order = [0] * n
min_val = 1e9
max_val = -1e9

def calculator():
    val = nums[1]
    for i in range(1, n):
        if order[i] == 0:
            val += nums[i+1]
        elif order[i] == 1:
            val -= nums[i+1]
        elif order[i] == 2:
            val *= nums[i+1]
        else:
            val = int(val / nums[i+1])
    return val
    

def pro(k):
    if k == n:
        global min_val, max_val
        value = calculator()
        min_val = min(value, min_val)
        max_val = max(value, max_val)
    
    global operator, order
    for cand in range(4):
        if operator[cand] >= 1:
            operator[cand] -= 1
            order[k] = cand
            pro(k + 1)
            operator[cand] += 1

pro(1)
print(max_val)
print(min_val)
