# 두 용액

N = int(input())
water = list(map(int,input().split()))

water.sort()
L,R = 0, N-1
result = 2000000001
total = 0
answer = []


#while L < R and L>=0 and R<N:
while L < R:
    
    total = water[L] + water[R]

    if abs(total) < result:
        result = abs(total)
        answer = [water[L],water[R]]
    
        if result == 0:
            break
        
    if total < 0: #음수
        L += 1
    else:
        R -=1


print(answer[0],answer[1])
