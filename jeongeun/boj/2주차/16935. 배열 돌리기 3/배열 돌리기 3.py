import sys

def rotate_90(matrix):
    return [[matrix[j][i] for j in reversed(range(len(matrix)))] for i in range(len(matrix[0]))]

def flip(matrix):
    return [row[::-1] for row in matrix]

def divide(array):
    n = len(array)
    m = len(array[0])
    return [array[i][:m//2] for i in range(n//2)], [array[i][m//2:] for i in range(n//2)], [array[i][:m//2] for i in range(n//2, n)], [array[i][m//2:] for i in range(n//2, n)]

def combine(q1, q2, q3, q4):
    upper = [i + j for i, j in zip(q1, q2)]
    lower = [i + j for i, j in zip(q3, q4)]
    return upper + lower

N, M, R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
operations = list(map(int, sys.stdin.readline().split()))

for op in operations:
    if op == 1:
        arr = flip(rotate_90(rotate_90(arr)))
    elif op == 2:
        arr = flip(arr)
    elif op == 3:
        N, M = M, N
        arr = rotate_90(arr)
    elif op == 4:
        N, M = M, N
        arr = rotate_90(rotate_90(rotate_90(arr)))
    elif op == 5:
        q1, q2, q3, q4 = divide(arr)
        arr = combine(q3, q1, q4, q2)
    elif op == 6:
        q1, q2, q3, q4 = divide(arr)
        arr = combine(q2, q4, q1, q3)

for row in arr:
    print(*row)