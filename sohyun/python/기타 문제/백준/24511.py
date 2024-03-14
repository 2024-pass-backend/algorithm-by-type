# 24511번: queuestack
# https://www.acmicpc.net/problem/24511
# 참고 그림 : https://burningfalls.github.io/algorithm/boj-24511/

import sys
from collections import deque

N = int(input())
seq_A = list(map(int,input().split())) # queue = 0 / stack = 1
seq_B = list(map(int, input().split()))
M = int(input())
seq_C = list(map(int, input().split()))

queue_ = deque([])
for i in range(N):
    if seq_A[i] == 0: #deque
        queue_.appendleft(seq_B[i])
if len(queue_) == 0:
    print(*seq_C)
    sys.exit() # 코드 즉시 종료
    
for c in seq_C:
    queue_.append(c)
    print(queue_.popleft(),end=' ')

'''
# 실패: 시간초과 발생
# 이유: res_B[i].pop(0)은 리스트의 맨 앞에서의 원소 삭제로 인해 매번 리스트의 원소들을 이동시켜 시간 복잡도가 높아짐.
# 해결방법: queue만 deque에 저장
N = int(input())
seq_A = list(map(int,input().split())) # queue = 0 / stack = 1
seq_B = list(map(int, input().split()))
M = int(input())
seq_C = list(map(int, input().split()))

res_B = [[x] for x in seq_B]
for c in seq_C:
    res = c
    for i in range(N):
        if seq_A[i] == 0:
            res_B[i].append(res)
            res = res_B[i].pop(0)
    print(res)
'''