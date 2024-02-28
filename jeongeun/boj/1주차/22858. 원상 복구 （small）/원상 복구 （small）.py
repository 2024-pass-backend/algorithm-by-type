N, K = map(int, input().split())
S = list(map(int, input().split()))
D = list(map(int, input().split()))

def unshuffle(s, d):
    result = [0] * N
    for i in range(N):
        result[d[i]-1] = s[i]
    return result

for _ in range(K):
    S = unshuffle(S, D)

print(*S)