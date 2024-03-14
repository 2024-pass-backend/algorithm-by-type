T = int(input())

for i in range(T):
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()
    
    L = 0
    result = 0

    for j in range(N):
        while True:
            if L==M or A[j] <= B[L]: 
                result += L
                break #while break
            else:
                L += 1
    print(result)
    