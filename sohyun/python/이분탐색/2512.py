# 예산
import sys
input = sys.stdin.readline

N = int(input())
money = list(map(int,input().split()))
M = int(input())

start = 0
end = max(money)
if sum(money) > M:
    
    while start <= end:
        mid = (start+end)//2
        total = 0

        for i in money:
            if i < mid:
                total += i
            else:
                total += mid

        if total > M:
            end = mid - 1
        elif total <= M:
            start = mid + 1
    print(end)
else:
    print(max(money))