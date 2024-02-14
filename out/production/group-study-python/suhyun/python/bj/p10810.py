n, m = tuple(map(int, input().split()))
s = [0] * (n+1)
##print(s)

for _ in range(m):
    i, j, k = tuple(map(int, input().split()))
    for x in range(i, j+1):
        s[x] = k

##print(s)
##print(len(s))

for i in range(1, len(s)):
    print(s[i], end=' ')