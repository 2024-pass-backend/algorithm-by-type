import math

def is_sosu(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

m = int(input())
n = int(input())
sum_val, min_val = 0, 0
first = False

for i in range(m, n+1):
    if i == 1:
        continue
    
    if is_sosu(i):
        sum_val += i
        if first == False:
            min_val = i
            first = True

if first == True:
    print(sum_val)

print(min_val if first == True else -1)


