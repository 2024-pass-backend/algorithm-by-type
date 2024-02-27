N, K = map(int, input().split()) # 5 2 
S = list(map(int, input().split())) # 4 1 3 5 2
D = list(map(int, input().split())) # 4 3 1 2 5

def unshuffle(s, d):
    result = [0] * N
    for i in range(N):
        result[d[i]-1] = s[i]
    return result

for _ in range(K):
    S = unshuffle(S, D)

print(*S)