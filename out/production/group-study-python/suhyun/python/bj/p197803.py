import math

n = int(input())
arr = list(map(int, input().split()))

def is_sosu(x):
    
    if x == 1:
        return False
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

count = 0

for elem in arr:
    if(is_sosu(elem)):
        count += 1

print(count)