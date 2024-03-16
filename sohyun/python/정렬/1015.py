# 수열 정렬
import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
sorted_array = sorted(array)

answer = []

for i in range(N):
    idx = sorted_array.index(array[i])
    answer.append(idx)
    sorted_array[idx] = -1

print(*answer)


'''
     value : 2 1 3 1
       idx : 0 1 2 3
sorted idx : 2 0 3 1
'''