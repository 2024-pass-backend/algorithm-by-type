n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
min_val, max_val = 1e9 + 1, -(1e9 + 1)

def calculators(operand1, select_operator, operand2):
    if select_operator == 0:
        return operand1 + operand2
    elif select_operator == 1:
        return operand1 - operand2
    elif select_operator == 2:
        return operand1 * operand2
    else:
        if operand1 < 0:
            operand1 = -operand1
            return -(int(operand1 / operand2))
        else:
            return int(operand1 / operand2)

def pro(idx, sum):
    if idx == n-1:
        global min_val, max_val
        min_val = min(min_val, sum)
        max_val = max(max_val, sum)
    
    else:        
        for cand in range(len(operators)):
            if operators[cand] >= 1:
                operators[cand] -= 1
                pro(idx + 1, calculators(sum, cand, nums[idx + 1]))
                operators[cand] += 1

pro(0, nums[0])
print(max_val)
print(min_val)
        