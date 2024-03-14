import sys
input = sys.stdin.readline

N,C = map(int,input().split())
House = [int(input()) for i in range(N)]
House.sort()
L,R = 1, House[N-1]-House[0] # 집들 사이의 최소 거리와 최대 거리로 설정!
result = 0
# 예외 처리해주기
if C == 2: 
    print(House[N-1]-House[0])
else:
    #while L <= R:
    while L < R:   
        M = (L+R)//2 # 공유기 설치 간격
        count = 1

        wifi = House[0]
        for i in range(N):
            if House[i] - wifi >= M:
                count += 1
                wifi = House[i]           
                
        if count < C : # 목표보다 작음 -> 간격을 줄여
            #R = M -1
            R = M
        elif count >= C:
            result = M
            L = M + 1
#print(result)
print(R)
