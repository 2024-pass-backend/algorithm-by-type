N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

A.sort()
B_ = sorted(B)

L = 0
result_dict = {}
'''
for i in range(M):
    while True:
        if L >= N:
            result_dict[B_[i]] = 0
            break
        elif B_[i] == A[L]:
            result_dict[B_[i]] = 1
            break
        L += 1
'''

'''
# ANSWER
for i in range(M):
    while L < N and B_[i] > A[L]:
        L += 1
    if L < N and B_[i] == A[L]:
        result_dict[B_[i]] = 1
    else:
        result_dict[B_[i]] = 0
'''
   
for i in range(M):
    print(result_dict[B[i]])