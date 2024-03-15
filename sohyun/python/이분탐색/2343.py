# 기타 레슨

N, M = map(int, input().split())
blues = list(map(int,input().split()))

start = max(blues)
end = sum(blues)

while start <= end:
    mid = (start+end)//2
    cnt = 1
    total = 0

    for blue in blues:
        if total + blue > mid:
            cnt += 1
            total = 0
        total += blue

    if cnt <= M:
        end = mid -1
    else:
        start = mid + 1
print(start)
