# +, -, x, / , 0 1 2 3
n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
selected = [0] * (n - 1)
min_val, max_val = 1e9 + 1, -(1e9 + 1)

def calculators():
    value = nums[0]
    idx = 0
    
    for i in selected:
        idx += 1
        if i == 0:
            value += nums[idx]
        elif i == 1:
            value -= nums[idx]
        elif i == 2:
            value *= nums[idx]
        else:
            if value < 0:
                value = -value
                value = int(value / nums[idx])
                value = -value
            else: 
                value = int(value / nums[idx])
    return value

def pro(idx):
    if idx == n-1:
        global min_val, max_val
        value = calculators()
        min_val = min(min_val, value)
        max_val = max(max_val, value)
    
    else:
        for cand in range(0, len(operators)):
            if operators[cand] >= 1:
                operators[cand] -= 1
                selected[idx] = cand
                pro(idx + 1)
                operators[cand] += 1

pro(0)
print(max_val)
print(min_val)