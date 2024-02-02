n = int(input())
nums = map(int, input().split())
sosu = 0

for elem in nums:
    false = 0
    if elem > 1:
        for i in range(2, elem):
            if elem % i == 0:
                false += 1
            
        if false == 0:
            sosu += 1

print(sosu)        