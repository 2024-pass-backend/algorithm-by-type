n = int(input())
arr = [int(input()) for i in range(n)]
arr.sort()

# mode : 지금까지의 최빈값
# modeCount : 최빈값의 등장횟수
# curCnt : 지금 보고 있는 숫자의 등장횟수
mode = arr[0] # 최빈값
modeCnt = 1
curCnt = 1

for i in range(1, n):
    if arr[i] == a[i - 1]:
        curCnt += 1
    else:
        curCnt = 1
    
    if modeCnt < curCnt:
        modeCnt = curCnt
        mode = arr[i]
    
print(mode)